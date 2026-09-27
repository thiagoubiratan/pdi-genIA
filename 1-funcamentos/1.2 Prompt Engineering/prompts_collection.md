# Coleção de Prompts Efetivos

Biblioteca pessoal de prompts testados e validados durante o PDI GenAI e no dia a dia de trabalho. Cada entrada inclui o contexto onde funcionou bem e o motivo do sucesso.

---

## Categoria: Estruturação / Especificidade

### Prompt: Explicação técnica com persona e formato definidos
**Contexto:** Pedir explicação de um conceito técnico (ex: API REST) para uso didático.

```
Você é um professor experiente explicando para um desenvolvedor iniciante.
Explique o conceito de API REST usando uma analogia do dia a dia (ex: 
garçom em um restaurante). Estruture a resposta em:
1. A analogia
2. Como ela se conecta ao conceito técnico
3. Um exemplo de código simples
```

**Por que funciona:** Definir a persona ("professor"), o público-alvo ("iniciante") e o formato de saída (passos numerados) produz respostas muito mais didáticas e previsíveis do que perguntas vagas como "explique API REST". Testado em comparação direta — o prompt estruturado foi claramente superior.

---

## Categoria: Few-shot (exemplos)

### Prompt: Classificação de sentimento
**Contexto:** Classificar frases como Positivo/Negativo/Neutro de forma consistente.

```
Classifique o sentimento das frases como Positivo, Negativo ou Neutro.

Frase: "Adorei o atendimento, super rápido!"
Sentimento: Positivo

Frase: "O produto chegou quebrado e ninguém me respondeu."
Sentimento: Negativo

Frase: "O pedido chegou no prazo informado."
Sentimento: Neutro

Frase: "[nova frase aqui]"
Sentimento:
```

**Por que funciona:** Os exemplos (few-shot) ancoram o formato e o critério de classificação esperado, reduzindo variação na resposta. Aumenta tokens de input, mas reduz tokens de output (resposta direta, sem explicações extras) — vale a pena em tarefas repetitivas e bem definidas.

---

## Categoria: Chain-of-thought (raciocínio)

### Prompt: Decisão com múltiplos critérios (ex: aprovação de PR)
**Contexto:** Cenário de agente de code review avaliando se um PR deve ser aprovado.

```
Um agente de code review encontrou 3 problemas de lint, 2 testes 
falhando e 1 violação de boas práticas. Pense passo a passo sobre 
a gravidade de cada problema antes de decidir se o PR deve ser aprovado.
```

**Por que funciona:** Forçar o raciocínio explícito ("pense passo a passo") antes da conclusão melhora a precisão em decisões com múltiplos critérios e torna a saída auditável — você vê o "porquê", não só o veredito. Custo: mais tokens de output. Para reduzir esse custo mantendo auditabilidade, é possível limitar o tamanho do raciocínio:

```
Pense passo a passo, mas seja conciso (máximo 3 linhas de raciocínio) 
antes de dar o veredito final.
```

---

## Categoria: Otimização de custo/latência

### Técnica: Prompt caching (cache_control ephemeral)
**Contexto:** Prompts de sistema longos e reutilizados com frequência (ex: instruções de uma skill de code review).

```
"system": [
  {
    "type": "text",
    "text": "[instruções longas e reutilizáveis da skill]",
    "cache_control": {"type": "ephemeral"}
  }
]
```

**Por que funciona:** Marca o bloco de sistema para ser reaproveitado entre chamadas, gerando ~90% de desconto nos tokens lidos do cache e reduzindo a latência em mais de 2x. Ideal para prompts de sistema estáveis (skills, agentes) que são chamados repetidamente com pouca variação.

---

## Notas gerais

- Few-shot: economiza tokens de **output**, custa mais tokens de **input**.
- Chain-of-thought: custa mais tokens de **output**, ganha em precisão e auditabilidade.
- Prompt caching: reduz custo e latência em prompts de sistema reutilizados — combina bem com CoT e few-shot quando o prompt base é fixo.
