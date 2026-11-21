# Few-shot examples

Zero-shot = descrever a tarefa. Few-shot = mostrar exemplos dela resolvida.

Caso usado: classificar commits em tipo (Conventional Commits) + severidade.

## Prompt 1 — zero-shot

```
Classifique meu commit com o tipo baseado em Conventional Commits
e com uma severidade.
```

Resultado: o modelo inventou a escala de severidade (`baixa/média/alta`),
o formato da resposta (campos rotulados com justificativa) e o critério
(risco de impacto). Nada disso estava no prompt.

## Prompt 2 — few-shot

```
Classifique commits em tipo (Conventional Commits) e severidade de 1 a 5.

A severidade mede o IMPACTO da mudança, não o tipo: risco de quebrar
algo em produção + alcance do que foi afetado. Um docs pode ser 4 e um
feat pode ser 2.

Responda apenas no formato: tipo-severidade

---

Commit: adiciona índice em pedidos.cliente_id; consulta do dashboard
cai de 3s para 50ms
Classificação: perf-4

Commit: corrige typo em "recomendacao" no README
Classificação: docs-1

Commit: adiciona campo opcional no payload, atrás de feature flag
desligada
Classificação: feat-2

Commit: documenta decisão de arquitetura de autenticação; define o
padrão que todos os serviços novos vão seguir
Classificação: docs-4

Commit: altera o cálculo de frete para todos os pedidos
Classificação: fix-5

---

Classifique estes três:

Commit: remove console.log esquecido no checkout
Classificação:

Commit: refatora a camada de repositório inteira, sem mudar
comportamento externo
Classificação:

Commit: sobe a versão do pydantic de 2.11 para 2.14
Classificação:
```

## Por que o segundo funciona melhor

Exemplo resolve três coisas que descrição não consegue dizer bem:

1. **Formato exato da saída** — cinco exemplos de `tipo-severidade` fixam
   isso melhor que "responda apenas com".
2. **Fronteira entre as classes** — onde termina 3 e começa 4 é difícil de
   descrever e fácil de demonstrar.
3. **Granularidade** — o exemplo fixa a escala sem precisar defini-la.

## Decisões de desenho do Prompt 2

- **A instrução define o critério, os exemplos definem a fronteira.**
  O parágrafo diz que severidade é impacto; os exemplos mostram onde
  ficam os limites.
- **Dois exemplos contrariam o mapeamento óbvio de propósito** (`docs-4`
  e `feat-2`). São os que mais ensinam, porque impedem a regra preguiçosa
  "feat sempre 5". Exemplo que confirma o esperado ensina pouco.
- **Classes balanceadas.** Exemplos concentrados numa faixa enviesam o
  resultado: três positivos e um negativo fazem o modelo pender para
  positivo em casos duvidosos.
- **Um caso ambíguo entre os itens a classificar** — o `build` de versão
  de biblioteca pode ser 1 (patch de rotina) ou 4 (lib central com
  breaking change). É ali que se descobre para que lado os exemplos puxam.

## A regra de ouro

**O exemplo é mais forte que a instrução.** Se os exemplos contradizem a
descrição, os exemplos ganham. Por isso exemplo mal escolhido é pior que
exemplo nenhum — ele ensina a regra errada em silêncio.

Foi o que aconteceu no meu primeiro esquema: eu havia definido
`feat-5, fix-4, refactor-3, docs-2` e 1 para o resto. Isso faz a
severidade ser calculada a partir do tipo — ou seja, não acrescenta
informação nenhuma, é o tipo escrito de outra forma. E classifica igual
um índice trivial e uma reescrita de query que derruba a latência de 3s
para 50ms.

## Quantos exemplos

Dois a cinco resolvem a maioria dos casos. Mais que isso só ajuda quando
a distinção é sutil (classificar ticket em 8 categorias parecidas, por
exemplo). Cada exemplo custa tokens em toda chamada — é o que motiva o
prompt caching, próximo item do PDI.
