# Chain-of-thought (CoT)

## 1. O que é

Pedir ao modelo que **raciocine antes de responder**, em vez de ir direto à
resposta final.

## 2. Por que funciona

O modelo gera um token por vez, e cada token gerado entra no contexto do
próximo. Exigir a resposta direta obriga a acertar o resultado final sem
nenhum passo intermediário onde se apoiar.

Os tokens de raciocínio funcionam como **rascunho**: `65 x 1800 = 117000`
fica escrito, e o passo seguinte lê isso em vez de recalcular. É a diferença
entre fazer a conta de cabeça e fazer no papel.

Daí o resultado conhecido:

| Tipo de tarefa | CoT ajuda? |
|---|---|
| Múltiplos passos (aritmética, lógica, análise com várias condições) | **Sim** |
| Um passo (classificar, extrair campo, traduzir) | **Não** |

## 3. A comparação (feita em 22/11/2026)

**Problema usado:** quantos chunks de 500 caracteres, com overlap de 100, saem
de um PDF de 65 páginas com 1800 caracteres por página?

### Versão A — sem CoT

> Prompt: *"Quantos chunks de 500 caracteres com overlap de 100 saem de um PDF
> de 65 páginas com 1800 caracteres por página? Responda apenas o número."*

```
293
```

**~1 token de output.**

### Versão B — com CoT

> Prompt: *"Mesmo problema. Pense passo a passo: (1) calcule o total de
> caracteres, (2) determine o passo da janela deslizante, (3) calcule o número
> de chunks, (4) dê a resposta final."*

```
1. Total de caracteres: 65 páginas x 1800 = 117.000 caracteres

2. Passo da janela: com chunk de 500 e overlap de 100, cada novo chunk
   avança 500 - 100 = 400 caracteres

3. Número de chunks: o primeiro chunk cobre 500 caracteres; os demais
   avançam 400 cada.
   ceil((117.000 - 500) / 400) + 1 = ceil(291,25) + 1 = 292 + 1 = 293

4. Resposta: 293 chunks
```

**~120 tokens de output.**

### O que mudou

| | Sem CoT | Com CoT |
|---|---|---|
| Resposta | 293 | 293 |
| Tokens de output | ~1 | ~120 |
| Custo relativo | 1x | ~120x |
| Latência | mínima | maior (gera mais texto) |
| Auditável? | não | sim — dá para conferir cada passo |

**O resultado foi o mesmo.** Veja a seção 5 para o porquê.

A diferença real não foi acurácia, foi **auditabilidade**: na versão B eu
consigo verificar que o passo 2 usou 400 e não 500, e pegar o erro se ele
estivesse lá. Na versão A eu recebo um número e tenho que confiar.

Conferi o 293 por fora, com uma simulação da janela deslizante em Python —
e é isso que a versão A não me deixa fazer sem refazer a conta inteira.

## 4. O trade-off: tokens de output

**O raciocínio é cobrado como output, e output é mais caro que input.** No
Claude Opus 5: **$5 por milhão de tokens de entrada, $25 por milhão de saída**
— 5x mais caro.

Comparando com o caching do item anterior:

| Técnica | Onde atua | Efeito |
|---|---|---|
| Prompt caching | **input** | economiza (leitura a 0,1x) |
| Chain-of-thought | **output** | gasta (5x o preço do input, e muito mais tokens) |

São os dois extremos da mesma conta. Caching barateia o que você manda; CoT
encarece o que você recebe.

## 5. O que mudou: thinking nativo

O CoT clássico — escrever *"pense passo a passo"* no prompt — nasceu porque os
modelos de 2022-2023 não raciocinavam sozinhos. **Os modelos atuais raciocinam
nativamente**, por parâmetro de API:

```python
thinking={"type": "adaptive"}          # o modelo decide quando e quanto pensar
output_config={"effort": "low"}        # low | medium | high | xhigh | max
```

Com `adaptive`, o modelo pensa muito num problema difícil e quase nada num
trivial, sem você precisar dizer nada.

**É por isso que as duas versões da comparação acima deram o mesmo resultado:**
o modelo raciocinou nos dois casos. Na versão A o raciocínio aconteceu
internamente e só o número final apareceu; na versão B ele foi escrito na
resposta visível. O trade-off não desapareceu — ele migrou do texto do prompt
para o parâmetro.

Consequências práticas:

- **Pedir "pense passo a passo" a um modelo com thinking ligado é redundante**,
  e pode deixar a resposta visível mais verbosa sem ganho de precisão.
- O raciocínio nativo **também é cobrado como output**. Controlar custo passa a
  ser questão de `effort`, não de prompt.
- CoT escrito no prompt continua útil em dois casos: quando você **não controla
  os parâmetros da API** (interface de chat, ferramenta de terceiros), ou
  quando quer uma **estrutura específica** de raciocínio ("primeiro liste as
  cláusulas, depois compare com a pergunta, depois responda").

## 6. Qual eu usaria em produção

**Depende de quem lê a resposta.**

- **Pipeline automatizado** (classificar commit, extrair campo, decidir rota):
  sem CoT. O raciocínio visível é desperdício — nada o consome, e eu pago 5x
  por token para gerar texto que vou descartar. Controlo a qualidade com
  `effort`, não com prompt.

- **Resposta que uma pessoa vai avaliar** (análise de contrato, diagnóstico de
  bug, recomendação): com raciocínio visível. O valor não é a precisão, é eu
  conseguir **auditar** como chegou lá. Num agente sobre PDF da LGPD, "o
  Art. 7º permite X porque Y" é verificável; "permite X" não é.

**A regra que eu levo:** CoT visível quando a resposta precisa ser **defendida**,
não quando precisa ser **precisa** — a precisão o thinking nativo já entrega.

## 7. Onde isso aparece no PDI

- **Fase 3.1 (Parâmetros de LLM):** `effort` e `thinking` são exatamente os
  parâmetros deste item. O trade-off "speed vs quality" do roteiro é este.
- **Fase 4 (Capstone):** o agente de PDF precisa citar a cláusula que embasa a
  resposta. Isso é CoT estruturado em formato de citação — e justifica o custo
  de output, porque é o que torna a resposta confiável.
