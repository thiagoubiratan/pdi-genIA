# Prompt caching

## 1. O que é

`cache_control: {"type": "ephemeral"}` marca um bloco de conteúdo para ser
guardado em cache. O modelo grava o processamento daquele trecho e, nas
chamadas seguintes, lê do cache em vez de reprocessar.

```python
system=[{
    "type": "text",
    "text": "<instruções + exemplos few-shot>",
    "cache_control": {"type": "ephemeral"}
}]
```

`ephemeral` = temporário. **TTL padrão: 5 minutos.** Existe
`{"type": "ephemeral", "ttl": "1h"}` para 1 hora, com gravação mais cara.

Limite: **máximo 4 marcadores** (`cache_control`) por requisição.

## 2. A regra do prefixo

**O cache é por prefixo.** Ele guarda desde o início do prompt até o ponto
marcado — e **qualquer byte diferente antes do marcador invalida tudo** depois
dele.

A ordem de montagem do prompt é fixa:

```
tools  →  system  →  messages
```

```
┌─────────────────────────────┬──────────────────┐
│   prefixo estável (cache)   │  parte variável  │
│   instruções + exemplos     │   a pergunta     │
└─────────────────────────────┴──────────────────┘
                              ↑ marcador aqui
```

Consequência prática: **o conteúdo estável tem que vir fisicamente antes do
variável.** Se um timestamp for interpolado no system prompt, tudo depois dele
fica impossível de cachear, não importa onde o marcador esteja.

### Os três invalidadores silenciosos

| Erro | Por que quebra |
|---|---|
| `datetime.now()` no system prompt | o prefixo muda a cada chamada |
| `uuid4()` / ID de requisição no começo | mesma coisa |
| `json.dumps(d)` sem `sort_keys=True` | ordem das chaves varia, bytes mudam |

Nenhum deles levanta exceção. O cache simplesmente nunca acerta — e isso só
aparece na fatura.

### Como conferir

```python
response.usage.cache_creation_input_tokens  # gravou   (pagou 1,25x)
response.usage.cache_read_input_tokens      # leu      (pagou 0,1x)
response.usage.input_tokens                 # não cacheado (preço cheio)
```

Se `cache_read_input_tokens` fica **zero** em chamadas repetidas com o mesmo
prefixo, há um invalidador silencioso. É o teste diagnóstico.

## 3. Custo e ponto de equilíbrio

| Operação | Preço relativo ao input normal |
|---|---|
| Gravar no cache (TTL 5 min) | **1,25x** |
| Gravar no cache (TTL 1 h) | **2x** |
| Ler do cache | **0,1x** |

Gravar é **mais caro** que não cachear; ler é 10x mais barato. Daí o ponto de
equilíbrio:

```
TTL 5min:  1,25 (grava) + 0,10 (lê)          = 1,35x   vs  2,00x sem cache
           -> compensa a partir da 2a chamada

TTL 1h:    2,00 (grava) + 0,20 (2 leituras)  = 2,20x   vs  3,00x sem cache
           -> compensa a partir da 3a chamada
```

**Prompt usado uma única vez: cachear sai mais caro.** O cache serve para
prefixo reutilizado.

### O mínimo de tokens (não é progressivo)

| Modelo | Mínimo para cachear |
|---|---|
| Claude Opus 5 | 512 tokens |
| Opus 4.8, Sonnet 5, Sonnet 4.6 | 1024 tokens |
| Opus 4.7 | 2048 tokens |
| Opus 4.6, Haiku 4.5 | 4096 tokens |

Repare que o mínimo **não cresce com a geração** — é 512 no modelo mais novo e
4096 no Opus 4.6. E prefixo abaixo do mínimo **não cacheia e não dá erro**:
você marca, acha que está cacheando, e não está.

## 4. Quando usar — o julgamento

**Por que o meu prompt few-shot de classificação de commits não se beneficia:**
ele tem cerca de 400 tokens (instrução + 5 exemplos). Isso está **abaixo do
mínimo de qualquer modelo**, então não cachearia nem se eu marcasse. E mesmo
que cacheasse, classificação é tipicamente uma chamada por commit, com
prefixo reutilizado poucas vezes dentro da janela de 5 minutos — perto do
ponto de equilíbrio, sem ganho claro.

**Qual parte do PDI se beneficia: a Fase 4 (Capstone).** No agente de
perguntas sobre PDF, cada pergunta envia os mesmos chunks recuperados do
documento junto da pergunta nova. Esse contexto é grande (milhares de tokens,
bem acima de qualquer mínimo) e **idêntico entre perguntas sobre o mesmo PDF**
— exatamente o caso de prefixo estável reutilizado. Numa conversa de 10
perguntas sobre o mesmo documento, 9 delas leem o contexto a 0,1x em vez de
pagar o preço cheio.

**A regra que eu levo:** cachear vale quando o prefixo é **grande**,
**idêntico** e **reutilizado** dentro da janela do TTL. Faltando qualquer um
dos três, não vale.

**Onde isso vai me morder:** o chunk recuperado muda conforme a pergunta (o
RAG busca chunks diferentes). Então o que eu posso cachear é a parte
realmente estável — instruções do agente e system prompt —, não o resultado
da busca. Montar o prompt na ordem certa (estável primeiro, chunk e pergunta
depois) é decisão de arquitetura da Fase 4, não detalhe de implementação.

## 5. Latência

Ler do cache é mais rápido que reprocessar — o modelo pula o prefill daquele
trecho.

Para a **primeira** chamada não pagar a lentidão da gravação, existe o
pré-aquecimento: uma requisição com `max_tokens: 0` no startup da aplicação.
Ela grava o cache e retorna na hora, sem gerar resposta.

Vale quando a latência da primeira resposta é visível para o usuário (chat,
voz). Não vale para job em lote, nem quando o tráfego é contínuo — aí a
primeira chamada real já aquece o cache sozinha.
