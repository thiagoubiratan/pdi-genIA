# Coleção de prompts efetivos

Acervo de consulta. Cada entrada traz o prompt pronto para copiar, quando
usar e a armadilha que ele evita.

Detalhamento de cada técnica nos arquivos de origem:
[princípios](1-principios_prompt.md) ·
[few-shot](2-few-shot.md) ·
[caching](3-prompt-caching.md) ·
[chain-of-thought](4-chain-of-thought.md)

---

## Checklist — rodar antes de enviar qualquer prompt

Os quatro eixos. Toda dúvida que sobrar é uma instrução que falta.

| Eixo | Pergunta que responde |
|---|---|
| **Tarefa** | Que verbo? Resumir, classificar, extrair, reescrever, comparar? |
| **Formato** | Como a saída sai? Lista, JSON, tabela, parágrafo? Quantos itens? |
| **Público** | Para quem? Define vocabulário e, mais importante, **o que entra e o que sai** |
| **Restrições** | Limite de tamanho, o que preservar, o que omitir |

**O eixo que mais surpreende é o público** — ele muda o *conteúdo*, não só o
estilo. Ver a comparação na seção "Descrição de PR" abaixo.

Teste rápido: *"se eu entregasse isso a um estagiário competente que não me
conhece, ele saberia exatamente o que fazer?"*

---

## 1. Estruturação — descrição de PR

### ❌ Vago

```
escreva uma descrição de PR pra mim
```

Resultado: o modelo inventou o idioma, o tamanho, as seções, o público, se
incluía comandos de teste, e omitiu risco e prazo. **Sete decisões tomadas
no meu lugar; cinco mudaram quando eu especifiquei.**

### ✅ Específico

```
Escreva uma descrição de PR no formato conventional commit.
Quem vai avaliar é o líder técnico do projeto.
Formato resumido, em tópicos.
```

**O que mudou além do formato:** saiu a descrição arquivo-por-arquivo
(irrelevante para quem decide aprovar) e entraram seções de **Impacto**,
**Validação** e **Pendências** — informação que a primeira versão não tinha.
Definir o público trocou o conteúdo.

**Quando usar:** qualquer pedido onde o leitor da saída não é você.

---

## 2. Few-shot — classificação

### Estrutura

```
<instrução com o critério>

Responda apenas no formato: <formato exato>

---

<Entrada>: exemplo 1
<Saída>: classificação 1

<Entrada>: exemplo 2
<Saída>: classificação 2

---

Classifique:
<Entrada>: item real
<Saída>:
```

### Exemplo completo — commit → tipo + severidade

```
Classifique commits em tipo (Conventional Commits) e severidade de 1 a 5.

A severidade mede o IMPACTO da mudança, não o tipo: risco de quebrar algo
em produção + alcance do que foi afetado. Um docs pode ser 4 e um feat
pode ser 2.

Responda apenas no formato: tipo-severidade

---

Commit: adiciona índice em pedidos.cliente_id; consulta do dashboard cai
de 3s para 50ms
Classificação: perf-4

Commit: corrige typo em "recomendacao" no README
Classificação: docs-1

Commit: adiciona campo opcional no payload, atrás de feature flag desligada
Classificação: feat-2

Commit: documenta decisão de arquitetura de autenticação; define o padrão
que todos os serviços novos vão seguir
Classificação: docs-4

Commit: altera o cálculo de frete para todos os pedidos
Classificação: fix-5

---

Classifique:
Commit: <o commit real>
Classificação:
```

### As três regras

1. **A instrução define o critério; os exemplos definem a fronteira.** Onde
   termina 3 e começa 4 é difícil de descrever e fácil de demonstrar.
2. **Inclua exemplos que contrariam o óbvio** (`docs-4`, `feat-2`). São os que
   mais ensinam — impedem a regra preguiçosa "feat sempre 5".
3. **Balanceie as classes.** Exemplos concentrados numa faixa enviesam o
   resultado.

### ⚠️ A armadilha que eu caí

Meu primeiro esquema foi `feat-5, fix-4, refactor-3, docs-2` e 1 para o resto.
Isso faz a severidade ser **calculada a partir do tipo** — ou seja, não
acrescenta informação nenhuma, é o tipo escrito de outra forma. E classifica
igual um índice trivial e uma reescrita de query que derruba a latência de 3s
para 50ms.

**Exemplo mal escolhido é pior que exemplo nenhum** — ensina a regra errada
em silêncio.

### Quantos

Dois a cinco. Mais só ajuda em distinção sutil (8 categorias parecidas).
Cada exemplo custa tokens em **toda** chamada.

---

## 3. Chain-of-thought — raciocínio visível

### Estrutura

```
<problema>

Pense passo a passo:
(1) <primeiro passo>
(2) <segundo passo>
(3) <terceiro passo>
(4) dê a resposta final
```

### Quando usar — a regra

> **CoT visível quando a resposta precisa ser defendida, não quando precisa
> ser precisa.**

A precisão o thinking nativo já entrega. O que o CoT visível compra é
**auditabilidade**.

| Contexto | Usar? | Por quê |
|---|---|---|
| Pipeline automatizado (classificar, extrair, rotear) | ❌ | Nada consome o raciocínio; pago 5x por token de output descartado |
| Resposta que uma pessoa avalia (análise, diagnóstico) | ✅ | Preciso auditar como chegou lá |
| Agente que cita fonte ("Art. 7º permite X porque Y") | ✅ | A citação é o que torna a resposta confiável |

### ⚠️ Redundante em modelo com thinking nativo

Os modelos atuais raciocinam sozinhos:

```python
thinking={"type": "adaptive"}       # o modelo decide quando e quanto pensar
output_config={"effort": "low"}     # low | medium | high | xhigh | max
```

Pedir *"pense passo a passo"* aí é redundante e deixa a resposta visível mais
verbosa sem ganho de precisão. **Controle custo com `effort`, não com prompt.**

CoT escrito continua útil em dois casos: quando você **não controla os
parâmetros da API** (interface de chat, ferramenta de terceiros), ou quando
quer uma **estrutura específica** de raciocínio.

---

## 4. Caching — prefixo estável

### Estrutura

```python
system=[{
    "type": "text",
    "text": "<instruções + exemplos few-shot>",   # estável
    "cache_control": {"type": "ephemeral"}        # marcador aqui
}]
messages=[{"role": "user", "content": pergunta}]  # variável, depois do marcador
```

### A regra

Cache é **por prefixo**. Ordem de montagem: `tools` → `system` → `messages`.
Qualquer byte diferente **antes** do marcador invalida tudo depois.

**Conteúdo estável vem fisicamente antes do variável.**

### Vale a pena quando

Prefixo **grande** + **idêntico** + **reutilizado** na janela do TTL (5 min
padrão). Faltando um dos três, não vale.

| | Custo relativo ao input normal |
|---|---|
| Gravar (TTL 5min) | 1,25x |
| Ler | 0,1x |

Compensa a partir da 2ª chamada. **Prompt usado uma vez: cachear sai mais caro.**

### ⚠️ Os três invalidadores silenciosos

| Erro | Por que quebra |
|---|---|
| `datetime.now()` no system prompt | prefixo muda a cada chamada |
| `uuid4()` / ID de requisição no começo | mesma coisa |
| `json.dumps(d)` sem `sort_keys=True` | ordem das chaves varia |

Nenhum levanta exceção. Diagnóstico:

```python
response.usage.cache_read_input_tokens   # zero em chamadas repetidas = invalidador
```

### ⚠️ O mínimo de tokens (não é progressivo)

| Modelo | Mínimo |
|---|---|
| Claude Opus 5 | 512 |
| Opus 4.8, Sonnet 5, Sonnet 4.6 | 1024 |
| Opus 4.7 | 2048 |
| Opus 4.6, Haiku 4.5 | 4096 |

Prefixo abaixo do mínimo **não cacheia e não dá erro**. Meu prompt few-shot de
commits (~400 tokens) está abaixo de qualquer um deles.

---

## As duas técnicas são opostas na conta

| Técnica | Onde atua | Efeito |
|---|---|---|
| Prompt caching | **input** | economiza (leitura a 0,1x) |
| Chain-of-thought | **output** | gasta (output é 5x o input, e são muitos tokens) |

Caching barateia o que você manda; CoT encarece o que você recebe.

---

## Para levar

1. **Prompt vago não dá resposta ruim — dá a resposta mais provável.** Se o seu
   caso não é o mais comum, você recebe algo plausível e errado. E parece bom,
   então você não revisa.
2. **O exemplo é mais forte que a instrução.** Se contradizem, o exemplo ganha.
3. **Definir o público muda o conteúdo**, não só o tom.
4. **O que era técnica de prompt virou parâmetro de API.** CoT → `thinking`;
   controle de custo → `effort`. Saber o conceito é o que permite escolher o
   parâmetro.
