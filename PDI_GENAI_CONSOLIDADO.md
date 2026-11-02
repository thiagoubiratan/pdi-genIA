# PDI - Desenvolvimento em GenAI & Agentes

**Data de início:** 26/10/2026  
**Data estimada de conclusão:** 13/12/2026 (7 semanas · 95h a 14h/semana)  
**Ritmo:** 14h/semana, com assistência do Claude Code — ver *Premissas da Estimativa*  
**Objetivo geral:** Dominar arquitetura de agentes GenAI com RAG, implementar sistema de produção capaz de processar e recuperar informações de PDFs com segurança e eficiência.

---

## Resumo Executivo

| Fase | Semanas | Horas | Horas acum. | Data de Entrega | Progresso | Foco | Status |
|------|---------|-------|-------------|-----------------|-----------|------|--------|
| 1: Fundamentos | 1-2 | 15,5h | 15,5h | **02/11/2026** (seg) | **10%** (1,5/15,5h) | Python, Streamlit, Prompt Eng | 🔄 Em andamento |
| 2: RAG | 2-3 | 23h | 38,5h | **14/11/2026** (sáb) | **0%** (0/23h) | Embeddings, Vector DB, Indexação | ⏳ Não iniciado |
| 3: Agentes | 3-6 | 37,5h | 76h | **03/12/2026** (qui) | **0%** (0/37,5h) | LLM Params, LangChain, Guardrails, MCP | ⏳ Não iniciado |
| 4: Capstone | 6-7 | 19h | 95h | **13/12/2026** (dom) | **0%** (0/19h) | Projeto integrado (Agente PDF) | ⏳ Não iniciado |

**Progresso geral: 1,6%** (1,5h de 95h concluídas)

**Tempo total estimado:** 95 horas (14h/semana por 7 semanas) · **banda realista: 7-9 semanas**

As datas de entrega derivam das **horas acumuladas** a 14h/semana desde 26/10/2026 — não de semanas cheias. Por isso elas caem no meio da semana: a Fase 1 consome 15,5h, ou seja, 1,5h além da Semana 1, e entrega na segunda da Semana 2. Se uma semana render menos que 14h, **todas as datas abaixo dela escorregam** — acompanhe as colunas *Entregue* / *Reais* / *Saldo* na tabela de Rastreamento Geral para saber o novo prazo.

**Como o Progresso é calculado:** soma das horas concluídas ÷ horas totais da fase. É **ponderado por horas**, não por contagem de itens — concluir "Criar MCP Server" (2h) vale 4× mais que "Max_tokens & stopping" (0,5h).

Itens 🔄 em andamento **contam proporcionalmente**: um item de 1,5h com 1 de 5 exercícios entregues soma 0,3h. Assim o indicador se move a cada entrega sua, em vez de ficar travado horas até o item fechar inteiro. **Mantido pelo Claude Code a cada item concluído**, sem precisar ser pedido. A atualização é em cascata: (1) emoji de Status do item na tabela da subseção, (2) coluna Progresso da fase aqui no Resumo Executivo, (3) linha Progresso geral, (4) colunas *Entregue* / *Reais* / *Saldo* em Horas por Semana, (5) nova linha no Registro de Horas por Sessão.

> Nota sobre a Fase 2 em 0%: os itens "Setup PostgreSQL" e "Instalação pgVector" estão ✅, mas foram reorçados para **0h** porque a infra já existe (ver 2.2). Zero horas concluídas de zero horas de trabalho — eles não movem o percentual e também não geram trabalho. Não é erro de cálculo.

---

## Premissas da Estimativa

*Revisão de 26/10/2026.*

As estimativas originais somavam **~163h** (133,5h nas tabelas de itens das Fases 1-3 + ~30h implícitas de Capstone) e assumiam estudo solo a 5-8h/semana. O cabeçalho antigo dizia "100-130h" e a tabela semanal "115h" — os três números não fechavam entre si. Esta revisão parte das **tabelas de itens**, que são a fonte real, e assume:

- **14h/semana** de dedicação (≈2h/dia, ou 3,5h × 4 dias).
- **Assistência do Claude Code em postura de professor**, no modo acordado: *aula com exemplos de código e saída esperada → perguntas de verificação antes de codificar → você escreve o código → eu reviso*. Não é despachar enunciado: o exercício vem depois da aula e serve para comprovar o que foi ensinado.
- **Você executa o setup e a infraestrutura, não só os exercícios.** Criar o venv, declarar dependências, subir container, criar schema e índice são conteúdo do PDI — eu explico o que cada comando faz e por quê, e confiro o resultado, mas quem roda é você. *(Regra acrescentada em 26/10/2026, depois de eu ter entregado o setup do ambiente pronto — corrigido: o setup foi desfeito para você refazer.)*

O fator de redução **não é uniforme** — depende do tipo de trabalho:

| Tipo de item | Redução | Por quê |
|---|---|---|
| Setup e infraestrutura | -40% | Docker, pgVector, schema, scaffolding: **você roda os comandos**; eu explico o porquê de cada um e valido o resultado na hora. O ganho vem de não caçar documentação nem depurar erro de ambiente — não de receber pronto. |
| Documentos e comparações | -50% | Eu gero o rascunho da tabela/documento; você valida, corrige e assina. |
| Código de integração | -45% | Pipelines, clients, tools, testes: escrevo o esqueleto, você ajusta e entende. |
| Exercícios de aprendizado | -25% | Você continua escrevendo o código. O ganho vem de não ficar travado em bug ou documentação — **não** de pular a prática. |
| Absorção conceitual | -25% | Explicação direta substitui caça em documentação, mas entender leva o tempo que leva. |

**Resultado:** ~163h → **95h** (-42%).

O prazo é dominado pelas **53h das Fases 1 e 3** — aprendizado e prática de código, que comprimem pouco. Infraestrutura, o item mais barato, responde por ~3h do total. É por isso que ter o PostgreSQL já instalado quase não muda a data: a economia apareceria em horas de *instalação*, não em horas de *entendimento*.

⚠️ **Por que a banda é 7-9 semanas, e não 7 fechadas:** 14h/semana sustentadas por 7 semanas seguidas é agressivo se concorrer com trabalho full-time, e aprendizado conceitual não escala linearmente com horas/semana — fadiga e consolidação precisam de intervalo. Se uma semana cair para 8-10h, a conclusão escorrega para o fim de dezembro. As horas de *código* comprimem bem; as de *entendimento*, menos.

---

## FASE 1: Fundamentos (Semanas 1-2 · 15,5h)

**Objetivo:** Construir base sólida em Python, redes neurais e prompt engineering para compreender o que vem depois.

### 1.1 Python + Streamlit

**Data de início:** 26/10/2026

**Descrição:** Dominar o essencial de Python para dados e criar UIs de prototipagem rápida.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Setup ambiente Python | ✅ | [Streamlit Docs](https://docs.streamlit.io) | Venv + requirements.txt + README.md | 0,5h |
| Bloco 1 — Base Python | ✅ | Documentação + prática | Exercícios com variáveis, tipos, condicionais, loops, funções e imports | 1,5h |
| Bloco 2 — Python específico | ⏳ | Documentação + prática | Exercícios com list comprehensions, lambda, arquivos, try/except e f-strings | 2h |
| Bloco 3 — Python avançado | ⏳ | Documentação + prática | Exercícios com classes, decorators, async/await e tipagem com Pydantic | 3h |
| Introdução Streamlit | ⏳ | [Getting Started](https://docs.streamlit.io/get-started) | App com 3 widgets (input, slider, button) | 1h |
| App interativo básico | ⏳ | [Streamlit Docs](https://docs.streamlit.io) | Calculadora com estado | 1,5h |

**Subtotal 1.1:** 9,5h *(original: 13,5h)*

**Convenção de pastas:** criadas sob demanda, quando o primeiro arquivo de cada uma nascer — não todas de antemão. O git não versiona diretório vazio, então pasta sem arquivo não existe para quem clona o repo. Nomes sem espaço e sem acento (`1.1-python-streamlit`, não `"1.1 Python + Streamlit"`), para não exigir aspas em comando de shell e de git.

**Marcos de conclusão:**
- ⏳ `streamlit run app.py` funciona sem erros
- ⏳ App com `st.text_input()` + `st.button()` + `st.write()` respondendo
- ⏳ Código commitado em repositório
- ⏳ Consegue escrever funções, manipular listas e tratar exceções em Python
- ⏳ Consegue criar uma classe simples e usar async/await

**Notas:**
```
[espaço para anotações]
```

---

### 1.2 Prompt Engineering

**Descrição:** Dominar técnicas de prompt para extrair máximo valor de LLMs.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Princípios de prompting | ⏳ | [Claude Prompt Engineering Guide](https://platform.claude.com/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Checklist: clareza, contexto, estrutura | 1,5h |
| Few-shot examples | ⏳ | Documentação + prática | Teste de classificação de sentimento com exemplos | 1,5h |
| Prompt caching | ⏳ | Documentação Anthropic | Entendimento de cache_control (ephemeral), custo e latência | 0,5h |
| Chain-of-thought | ⏳ | Documentação + experimentação | Comparação com vs sem CoT, trade-off de tokens de output | 1,5h |
| Coleta de prompts efetivos | ⏳ | Seu acervo | `prompts_collection.md` com exemplos categorizados (estruturação, few-shot, CoT, caching) | 1h |

**Subtotal 1.2:** 6h *(original: 9h)*

**Marcos de conclusão:**
- ⏳ Entender princípios de especificidade, persona/contexto, formato de saída e divisão em passos
- ⏳ Conseguir melhorar resultado de um prompt adicionando contexto/exemplos (few-shot)
- ⏳ Entender prompt caching e seu impacto em custo/latência
- ⏳ Entender quando usar CoT vs direct prompting (e como controlar o tamanho do raciocínio)
- ⏳ Arquivo `prompts_collection.md` com exemplos funcionais

**Notas:**
```
[espaço para anotações]
```

---

### Checklist Fase 1

- [ ] Streamlit app rodando localmente
- [ ] Bloco 1 Python concluído
- [ ] Bloco 2 Python concluído
- [ ] Bloco 3 Python concluído
- [ ] Coleção de prompts efetivos
- [ ] Código commitado com README
- [ ] **Verificação:** Consegue explicar 3 conceitos sem notas? ✅

**Conclusão da Fase 1:** Data estimada: 02/11/2026 | Data real: _________

---

## FASE 2: RAG (Retrieval-Augmented Generation) — Semanas 2-3 · 23h

**Objetivo:** Implementar pipeline completo de indexação e recuperação de informações com vector databases.

### 2.1 Embeddings & Modelos

**Descrição:** Entender como textos são convertidos em vetores e quais modelos usar.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| O que são embeddings | ⏳ | [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings) | Documento: dimensionality, cosine similarity, use cases | 1,5h |
| Testar modelos | ⏳ | Hugging Face + OpenAI + código próprio | Comparação: 3 modelos (OpenAI, sentence-transformers, open-source) | 2h |
| Comparar resultados | ⏳ | Notebooks | Tabela: speed, dimensão, qualidade, custo | 1h |

**Subtotal 2.1:** 4,5h *(original: 8h)*

**Marcos de conclusão:**
- ⏳ Script que gera embeddings com 3 modelos diferentes
- ⏳ Entender trade-off entre dimensionalidade e qualidade
- ⏳ Decidir qual modelo usar no seu projeto

**Notas:**
```
[espaço para anotações]
```

---

### 2.2 Vector Database - pgVector

**Descrição:** Setup de PostgreSQL + pgVector para armazenar e buscar embeddings.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Setup PostgreSQL local | ⏳ | Docker ou instalação nativa | PostgreSQL rodando na porta 5432 | 0,5h |
| Instalação pgVector | ⏳ | [pgVector GitHub](https://github.com/pgvector/pgvector) | Extensão instalada e criada | 0,5h |
| Schema básico | ⏳ | SQL + documentação | Tabela com colunas: id, content, embedding (vector) | 0,5h |
| Queries básicas | ⏳ | Experimentação | Scripts: INSERT, cosine similarity search | 1h |
| Índices para performance | ⏳ | pgVector docs | HNSW ou IVFFlat index criado | 0,5h |

**Subtotal 2.2:** 3h *(original: 7h)*

**Infra já disponível** (verificado em 26/10/2026 — sobreviveu ao reset, porque o reset apagou código, não o banco):

| Componente | Estado |
|---|---|
| Container | `pdi-postgres` · imagem `pgvector/pgvector:pg17` |
| Extensão | `vector 0.8.7` no database `pdi_rag` |
| Tabelas | `chunks_lgpd` (287 linhas, `vector(384)`) e `documentos` (4 linhas) |
| Índices | HNSW `vector_cosine_ops` em ambas |

Credenciais usadas pelos scripts: `localhost:5432`, db `pdi_rag`, user `postgres`, senha `pdi123`.

⚠️ **Na Semana 2 você refaz isso do zero**, pela regra de que a infraestrutura é sua: derrubar e recriar o container com a imagem `pgvector/pgvector`, rodar `CREATE EXTENSION vector`, escrever o `CREATE TABLE` com a coluna `vector(384)` e o `CREATE INDEX ... USING hnsw`. A infra atual serve de **gabarito de conferência** — no fim, o que você montou tem que casar com a tabela acima. Custo: as 3h orçadas em 2.2.

**Marcos de conclusão:**
- ⏳ PostgreSQL + pgVector rodando `SELECT 1;` e `CREATE EXTENSION vector;` funcionam
- ⏳ Tabela criada com coluna vector
- ⏳ Query de busca por similitude retornando resultados
- ⏳ Índice criado, query <100ms para 10k vetores

**Notas:**
```
[espaço para anotações]
```

---

### 2.3 Indexação: PDF → Chunks → Embeddings → pgVector

**Descrição:** Pipeline completo de ingestão de PDFs.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Leitura de PDF | ⏳ | PyPDF2 ou pdfplumber | Script que extrai texto de PDF | 0,5h |
| Chunking estratégias | ⏳ | LangChain docs + experimentação | 3 estratégias testadas (fixed size, semantic, overlap) | 2h |
| Geração de embeddings | ⏳ | Seu código | Script que chama API de embeddings | 1h |
| Inserção em pgVector | ⏳ | psycopg2 ou SQLAlchemy | Inserir batch de embeddings | 1h |
| Pipeline integrado | ⏳ | Seu código | Script: `python ingest.py docs/sample.pdf` → pgVector | 1,5h |

**Subtotal 2.3:** 6h *(original: 11h)*

**Marcos de conclusão:**
- ⏳ PDF lido e dividido em chunks
- ⏳ Embeddings gerados (local ou via API)
- ⏳ Dados inseridos em pgVector
- ⏳ Query retorna chunks relevantes

**Notas:**
```
[espaço para anotações]
```

---

### 2.4 Retrieval & Ranking

**Descrição:** Melhorar qualidade de busca além de similaridade vetorial.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Busca por similaridade | ⏳ | pgVector + Python | Query base: `ORDER BY embedding <-> query_embedding LIMIT 5` | 0,5h |
| BM25 (hybrid search) | ⏳ | Implementação + documentação | Combinar keyword search + vector search | 2h |
| Reranking | ⏳ | Biblioteca como `rank-bm25` | Reordenar top-k resultados por relevância | 1h |
| Avaliação de qualidade | ⏳ | Teste manual + métricas | Documento comparando 3 estratégias em 5 queries | 2h |

**Subtotal 2.4:** 5,5h *(original: 9h)*

**Marcos de conclusão:**
- ⏳ Implementado busca por similaridade pura
- ⏳ Adicionado BM25 para hybrid search
- ⏳ Avaliação: métrica de qualidade (ex: NDCG, MRR)
- ⏳ Documentação de qual estratégia usar quando

**Notas:**
```
[espaço para anotações]
```

---

### 2.5 Graph RAG vs Vector RAG

**Descrição:** Entender diferenças e quando usar cada abordagem.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Conceitos Graph RAG | ⏳ | [Seu vídeo](https://www.youtube.com/watch?v=_HQ2H_0Ayy0) | Notas: entities, relationships, queries | 1,5h |
| Comparação Vector vs Graph | ⏳ | Pesquisa própria | Documento: quando usar cada, trade-offs | 1h |
| Experimento básico | ⏳ | Neo4j ou equivalente (opcional) | Prototipo simples comparando resultados | 1,5h |

**Subtotal 2.5:** 4h *(original: 6h)*

**Marcos de conclusão:**
- ⏳ Documento explicando Vector RAG, Graph RAG e hybrid
- ⏳ Decisão tomada: qual usar no seu projeto Capstone
- ⏳ Argumentação documentada

**Notas:**
```
[espaço para anotações]
```

---

### Checklist Fase 2

- [ ] Modelos de embedding testados e comparados
- [ ] PostgreSQL + pgVector rodando
- [ ] Pipeline de indexação funcionando (PDF → pgVector)
- [ ] Busca retornando resultados relevantes
- [ ] Hybrid search (vector + BM25) implementado
- [ ] Documento Vector vs Graph RAG
- [ ] Código commitado
- [ ] **Verificação:** Consegue buscar e recuperar chunks relevantes? ✅

**Conclusão da Fase 2:** Data estimada: 14/11/2026 | Data real: _________

---

## FASE 3: Agentes & LLM Orchestration - (MCP) — Semanas 3-6 · 37,5h

**Objetivo:** Orquestrar chamadas a LLMs com estado, memória e raciocínio multi-turno.

### 3.1 Parâmetros de LLM

**Descrição:** Dominar como tunar temperatura, top-p, max_tokens para diferentes casos de uso.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Temperature & Randomness | ⏳ | Claude API docs + experimentação | Documento: T=0 vs T=1, casos de uso | 1h |
| Top-p, Top-k, Frequency Penalty | ⏳ | Claude API docs | Documento explicando cada parâmetro | 1h |
| Max_tokens & stopping | ⏳ | Experiência | Guidelines para seu projeto | 0,5h |
| Testes comparativos | ⏳ | Script de testes | 5 prompts com 3 configs diferentes, comparar resultados | 1,5h |

**Subtotal 3.1:** 4h *(original: 8h)*

**Marcos de conclusão:**
- ⏳ Documento com recomendações de parâmetros por case (análise, criação, raciocínio)
- ⏳ Script que testa diferentes configs
- ⏳ Entender trade-off speed vs quality

**Notas:**
```
[espaço para anotações]
```

---

### 3.2 LangChain Fundamentals

**Descrição:** Começar com chains básicas antes de agents complexos.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Setup LangChain | ⏳ | [LangChain Docs](https://docs.langchain.com) | Projeto base estruturado | 0,5h |
| LLMChain simples | ⏳ | Tutorial official | Chain: input → LLM → output | 1h |
| PromptTemplate | ⏳ | Docs + código | 3 templates para diferentes tarefas | 1h |
| Chain com memória | ⏳ | LangChain Memory docs | Chain que mantém histórico conversacional | 2h |
| Chain com tools | ⏳ | LangChain Tools docs | Chain que chama função Python (ex: cálculo) | 2h |

**Subtotal 3.2:** 6,5h *(original: 11h)*

**Marcos de conclusão:**
- ⏳ Estrutura de projeto com LangChain
- ⏳ Pelo menos 3 chains funcionando
- ⏳ Memory funcionando (conversa multi-turno)
- ⏳ Tools sendo invocadas corretamente

**Notas:**
```
[espaço para anotações]
```

---

### 3.3 LangGraph (Agentic Loops)

**Descrição:** Implementar agents com estados e raciocínio iterativo.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Conceito de State Machines | ⏳ | LangGraph docs | Documento: estados, transitions | 1,5h |
| Primeiro graph simples | ⏳ | Documentação official | Agent com 2-3 estados rodando | 2,5h |
| Action nodes | ⏳ | Docs + código | Nodes que executam ações (tools) | 2h |
| Loops e condicionals | ⏳ | Experimentação | Agent que decide iterar ou parar | 2h |
| Visualização de graphs | ⏳ | LangGraph viz tools | Diagrama dos states funcionando | 0,5h |

**Subtotal 3.3:** 8,5h *(original: 14h)* — o item mais pesado do PDI depois do Capstone

**Marcos de conclusão:**
- ⏳ Agent com 3+ estados implementado
- ⏳ Agent consegue chamar tools e continuar loop
- ⏳ Condição de parada funcionando
- ⏳ Diagrama de estados visualizado

**Notas:**
```
[espaço para anotações]
```

---

### 3.4 Guardrails & Segurança

**Descrição:** Implementar validação de entrada e controle de saída.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Input validation | ⏳ | Pydantic + custom logic | Middleware que rejeita inputs malformados | 1h |
| Output filtering | ⏳ | Regex + classification | Verificar se resposta sai do escopo | 1h |
| Rate limiting | ⏳ | Biblioteca ou custom | Middleware que limita requisições | 0,5h |
| Injection prevention | ⏳ | Documentação + código | Proteção contra prompt injection | 1,5h |
| Logging & monitoring | ⏳ | Estrutura de logs | Registrar todas as requisições/respostas | 0,5h |

**Subtotal 3.4:** 4,5h *(original: 10h)* — injection prevention é o único que exige raciocínio adversarial seu; o resto é padrão conhecido

**Marcos de conclusão:**
- ⏳ Middleware de validação funcionando
- ⏳ Agent rejeita inputs fora do escopo
- ⏳ Rate limit implementado
- ⏳ Logs estruturados

**Notas:**
```
[espaço para anotações]
```

---

### 3.5 Memória: Curto & Longo Prazo

**Descrição:** Implementar memória em conversas multi-turno.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Short-term (conversa) | ⏳ | LangChain ConversationBufferMemory | Janela deslizante de mensagens | 1h |
| Long-term (embeddings) | ⏳ | Vector similarity + metadata | Recuperar contexto anterior relevante | 2h |
| Resumo automático | ⏳ | LLM para criar resumos | Sumarizar conversa antes de esquecer | 1h |
| Teste integrado | ⏳ | Script multi-turno | Conversa que referencia tópicos antigos | 1,5h |

**Subtotal 3.5:** 5,5h *(original: 10h)*

**Marcos de conclusão:**
- ⏳ Agent mantém contexto entre turnos
- ⏳ Agent consegue buscar e usar memória anterior
- ⏳ Resumo funciona
- ⏳ Teste com 10+ turnos mostrando continuidade

**Notas:**
```
[espaço para anotações]
```

---

### 3.6 MCP - Model Context Protocol

**Descrição:** Entender e implementar o protocolo padrão para conectar agentes de IA a ferramentas e fontes de dados externas de forma padronizada.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| O que é MCP e por que importa | ⏳ | [MCP Docs](https://modelcontextprotocol.io/introduction) | Documento: arquitetura host/client/server, casos de uso | 1h |
| Componentes do protocolo | ⏳ | Documentação oficial | Diagrama: Tools, Resources, Prompts e como interagem | 1h |
| Criar MCP Server simples | ⏳ | SDK Python (`mcp`) | Server com 1-2 tools expostas (ex: busca em arquivo local) | 2h |
| Conectar agent ao MCP Server | ⏳ | Claude API + MCP | Agent que descobre e invoca tools via protocolo | 2h |
| MCP com múltiplos servidores | ⏳ | Experimentação | Agent consumindo 2 servidores distintos simultaneamente | 1,5h |
| Segurança e controle de acesso | ⏳ | MCP Docs + código | Validação de permissões e escopos no servidor | 1h |

**Subtotal 3.6:** 8,5h *(original: 17h)* — você pode inspecionar os MCP servers que o Claude Code já usa como referência viva

**Marcos de conclusão:**
- ⏳ Documento explicando o papel do MCP no ecossistema de agentes
- ⏳ MCP Server funcional com ao menos 2 tools registradas
- ⏳ Agent invocando tools remotas via protocolo MCP
- ⏳ Diferença clara entre MCP e chamada direta de função documentada

**Notas:**
```
[espaço para anotações]
```

---

### Checklist Fase 3

- [ ] Parâmetros LLM documentados e testados
- [ ] LangChain chains implementadas (3+ tipos)
- [ ] LangGraph com state machine funcionando
- [ ] Agent consegue chamar tools e iterar
- [ ] Guardrails implementados (input/output validation)
- [ ] Rate limiting funcionando
- [ ] Memória curto + longo prazo funcionando
- [ ] MCP Server criado e conectado a um agent
- [ ] Código bem estruturado e testado
- [ ] **Verificação:** Agent consegue conversa 10+ turnos coerente? ✅

**Conclusão da Fase 3:** Data estimada: 03/12/2026 | Data real: _________

---

## FASE 4: Capstone - Agente PDF com RAG — Semanas 6-7 · 19h

**Objetivo:** Integrar tudo em um sistema pronto para produção.

### Especificação do Projeto

**Nome:** PDF Question Answering Agent  
**Descrição:** Sistema que permite upload de PDFs e responde perguntas sobre seu conteúdo usando RAG + agentes com memória e guardrails.

### 4.1 Requisitos Funcionais

- [ ] Upload de PDF via Streamlit UI
- [ ] Processamento automático: parse → chunking → embeddings → pgVector
- [ ] Agent que responde perguntas multi-turno sobre o PDF
- [ ] Recuperação de contexto via RAG
- [ ] Rejeição de perguntas fora do escopo
- [ ] Histórico de conversa mantido
- [ ] Logs de todas as operações

### 4.2 Estrutura de Código

```
pdf-agent/
├── README.md                    # Documentação geral
├── ARCHITECTURE.md              # Sua decisão de design
├── requirements.txt             # Dependências
├── .env.example                 # Variáveis de ambiente
│
├── src/
│   ├── __init__.py
│   ├── config.py                # Configurações globais
│   ├── logger.py                # Setup de logging
│   │
│   ├── pdf_processor/
│   │   ├── __init__.py
│   │   ├── loader.py            # Leitura de PDF
│   │   ├── chunker.py           # Estratégias de chunking
│   │   └── embedder.py          # Geração de embeddings
│   │
│   ├── vectorstore/
│   │   ├── __init__.py
│   │   ├── pgvector_client.py   # Conexão pgVector
│   │   ├── retriever.py         # Busca + reranking
│   │   └── migrations.py        # Setup de schema
│   │
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── tools.py             # Tools do agent (search, lookup)
│   │   ├── guardrails.py        # Validação entrada/saída
│   │   ├── memory.py            # Gerenciamento de memória
│   │   └── graph.py             # State machine do agent
│   │
│   └── ui/
│       ├── __init__.py
│       ├── app.py               # Streamlit main
│       └── components.py        # Widgets reutilizáveis
│
├── tests/
│   ├── __init__.py
│   ├── test_pdf_processor.py
│   ├── test_retriever.py
│   ├── test_agent.py
│   └── conftest.py              # Fixtures pytest
│
└── docs/
    ├── SETUP.md                 # Como rodar local
    ├── DEPLOYMENT.md            # Deploy em produção
    └── EXAMPLES.md              # Casos de uso
```

### 4.3 Implementação - Checklist Detalhado

**Total da Fase 4:** 19h *(original implícito: ~30h)*

**Sprint 1: Backend Base** — 3h
- [ ] Estrutura de pastas criada
- [ ] Config + logger setup
- [ ] PDF loader funcionando
- [ ] Chunking com 3 estratégias
- [ ] Embedder conectado a modelo escolhido

**Sprint 2: Vector Store** — 3h
- [ ] Migrations de schema rodam
- [ ] Inserção de embeddings funciona
- [ ] Retriever retorna top-k relevantes
- [ ] Reranking implementado
- [ ] Testes: retrieval@5, retrieval@10

**Sprint 3: Agent** — 4,5h
- [ ] Tools definidas (search, summary)
- [ ] LangGraph state machine criada
- [ ] Agent consegue chamar tools
- [ ] Memória implementada
- [ ] Guardrails bloqueando inputs inválidos

**Sprint 4: UI + Integração** — 3,5h
- [ ] Streamlit app com upload
- [ ] Chat interface para perguntas
- [ ] Exibição de chunks recuperados
- [ ] Histórico de conversa
- [ ] Tratamento de erros robusto

**Sprint 5: Testes + Docs** — 3h
- [ ] Testes unitários (>80% coverage)
- [ ] Testes de integração (3 cenários)
- [ ] README com instruções
- [ ] Documentação de arquitetura
- [ ] Exemplos de prompts

### 4.4 Casos de Uso para Teste — 2h

Prepare 3 PDFs reais para testar:

**PDF 1: Documentação técnica**
- Perguntas: "Como configurar X?", "Qual versão requer Y?"
- Esperado: Recuperar seções específicas com precisão

**PDF 2: Contrato/Legal**
- Perguntas: "Qual é o prazo de rescisão?", "Quais são as obrigações?"
- Esperado: Citar cláusulas exatas

**PDF 3: Research paper**
- Perguntas: "Qual foi a metodologia?", "Quais foram os resultados?"
- Esperado: Síntese de múltiplas seções

### 4.5 Métricas de Sucesso

| Métrica | Target | Verificação |
|---------|--------|------------|
| Latência P99 | <2s | Medir 100 queries |
| Retrieval accuracy | >80% | 10 queries testadas |
| Uptime | >99% | Rodar por 1h sem crashes |
| Memory cleanup | <1GB steady state | Monitor após 50 queries |
| Guardrail precision | >95% | 20 invalid inputs testados |

### 4.6 Deliverables Finais

- ⏳ Repositório git com histórico limpo
- ⏳ `README.md` com setup em 5 minutos
- ⏳ `.env.example` com todas as variáveis
- ⏳ `ARCHITECTURE.md` explicando decisões
- ⏳ Código funcionando: `streamlit run src/ui/app.py`
- ⏳ 3 PDFs de teste com 10+ perguntas cada
- ⏳ Testes passando: `pytest tests/`
- ⏳ Video de 3min ou documento mostrando 3 casos de uso

---

### Checklist Fase 4

- [ ] Estrutura de pastas criada
- [ ] PDF processor implementado
- [ ] Vector store conectado
- [ ] Agent criado e testado
- [ ] Streamlit UI funcionando
- [ ] Testes unitários passando
- [ ] Documentação completa
- [ ] 3 casos de uso testados
- [ ] Repo limpo e documentado
- [ ] **Verificação Final:** Consegue responder 5 perguntas coerentes sobre PDF desconhecido? ✅

**Conclusão da Fase 4:** Data estimada: 13/12/2026 | Data real: _________

---

## Rastreamento Geral de Progresso

### Timeline Visual

```
┌─ Semana 1-2: Fundamentos ───── 15,5h ─┐
│  🔄 Python              9,5h
│  ⏳ Prompting           6,0h
│
├─ Semana 2-3: RAG ────────────  23,0h ─┐
│  ⏳ Embeddings          4,5h
│  ⏳ pgVector            3,0h
│  ⏳ Indexação           6,0h
│  ⏳ Retrieval           5,5h
│  ⏳ Graph vs Vector     4,0h
│
├─ Semana 3-6: Agents ───────── 37,5h ─┐
│  ⏳ LLM Params          4,0h
│  ⏳ LangChain           6,5h
│  ⏳ LangGraph           8,5h
│  ⏳ Guardrails          4,5h
│  ⏳ Memory              5,5h
│  ⏳ MCP                 8,5h
│
└─ Semana 6-7: Capstone ──────── 19,0h ─┐
   ⏳ Backend + Vector store   6,0h
   ⏳ Agent                    4,5h
   ⏳ UI + Integração          3,5h
   ⏳ Testes + Docs            3,0h
   ⏳ Casos de uso             2,0h
```

### Horas por Semana

| Semana | Período | Fase | Planej. | Entregue | Reais | Saldo | Notas |
|--------|---------|------|---------|----------|-------|-------|-------|
| 1 | 26/10 – 01/11 | Fund. (1.1 + 1.2) | 14h | 0,8h | *a informar* | *a calcular* | Setup concluído; Bloco 1 em andamento (variáveis e tipos ✅, 1 de 5 exercícios) |
| 2 | 02/11 – 08/11 | Fund. (1.1 + 1.2) | 14h | 0,7h | - | - | Semana 1 entregou 0,8h de 14h. **Decisão de 02/11: datas mantidas**, reavaliar no fim desta semana. Bloco 1 ✅ concluído |
| 3 | 09/11 – 15/11 | RAG (2.3-2.5) → Agent | 14h | - | - | - | |
| 4 | 16/11 – 22/11 | Agent (3.1-3.3) | 14h | - | - | - | |
| 5 | 23/11 – 29/11 | Agent (3.3-3.5) | 14h | - | - | - | |
| 6 | 30/11 – 06/12 | Agent (3.6) → Capstone | 14h | - | - | - | |
| 7 | 07/12 – 13/12 | Capstone (Sprints 3-5) | 11h | - | - | - | |

**Total planejado:** 95h | **Total entregue:** 1,5h | **Total real:** *a informar* | **Saldo:** *a calcular*

**O que cada coluna mede:**

| Coluna | Definição |
|---|---|
| **Planej.** | Orçamento de horas da semana (14h, exceto a última) |
| **Entregue** | Soma das horas **orçadas** dos itens que fecharam ✅ na semana — é o que move a coluna Progresso |
| **Reais** | Tempo de relógio efetivamente gasto |
| **Saldo** | `Entregue − Reais`. **Positivo = adiantado** (gastou menos que o orçado); negativo = atrasado |

Por que não comparar *Reais* direto com *Planej.*: no meio da semana isso sempre pareceria atraso, porque as 14h ainda não foram consumidas. `Entregue − Reais` é honesto em qualquer momento da semana. Um saldo negativo persistente é o sinal de que as estimativas em *Premissas da Estimativa* estão otimistas e precisam ser revistas — não de que você precisa estudar mais rápido.

### Registro de Horas por Sessão

| Data | Item do roteiro | Orçado | Real | Observação |
|------|-----------------|--------|------|------------|
| 26/10/2026 | *(meta) Revisão do plano* | — | — | Revisão das estimativas para 14h/semana, datas de entrega, coluna de progresso e registro de horas. Não é item do roteiro — preencher se quiser contabilizar |
| 26/10/2026 | ~~1.1 Setup ambiente Python~~ | ~~0,5h~~ | ~~0,1h~~ | **Anulado.** Eu havia executado o setup; desfeito para o Thiago refazer, conforme a regra em *Premissas da Estimativa* |
| 27/10/2026 | 1.1 Setup ambiente Python ✅ | 0,5h | *a informar* | Refeito pelo Thiago: venv + 2 pacotes, `requirements.txt` declarado à mão, `README.md`. Pastas passaram a ser criadas sob demanda |
| 27/10/2026 | 1.1 Bloco 1 — variáveis e tipos 🔄 | 0,3h | *a informar* | `bloco1/variaveis.py` aprovado: escalares, `type()`, `list` com índice e `len()`, conversão com `str()`/`int()`. Aprendidos na prática: `int()` trunca (1,78 → 1) e `print` com vírgula dispensa `str()` (tipagem forte barra `"x " + 65`) |
| 02/11/2026 | 1.1 Bloco 1 — Base Python ✅ | 0,7h | *a informar* | `bloco1/catalogo.py` aprovado (10 passos): condicionais, `for`/`enumerate`, `while`, `range`, funções com `return` e valor padrão, `import math`, operador `and`. Conceito-chave depurado: **escopo de função** — atribuir a um nome dentro de `def` torna-o local e causa `UnboundLocalError`; `if`/`for` não criam escopo. Comparação com C# (campo de classe vs `global`/`self`) acelerou o entendimento. Incômodo deixado de propósito: 3 listas paralelas coordenadas por índice → motiva `dict` |

⚠️ **O "Real" acima cobre só o tempo de execução que eu medi.** Não tenho como medir seu tempo de leitura, decisão e estudo — ao fim de cada sessão eu pergunto quanto tempo você gastou e registro aqui. Se o número de hoje estiver subestimado, me diga o valor correto que eu ajusto a linha e o saldo.

As fases não se alinham às bordas das semanas — a Semana 2 fecha a Fase 1 e já começa a Fase 2, por exemplo. Isso é intencional: o controle é por **horas acumuladas**, não por semana cheia.

---

## Recursos Consolidados

### Documentação Oficial
- [Claude Prompting Best Practices](https://platform.claude.com/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [LangChain Documentation](https://docs.langchain.com)
- [LangGraph Documentation](https://python.langchain.com/docs/concepts/architecture)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)
- [Streamlit Docs](https://docs.streamlit.io)
- [pgVector GitHub](https://github.com/pgvector/pgvector)

### Vídeos
- [3Blue1Brown - Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk)
- [RAG Concepts](https://www.youtube.com/watch?v=_HQ2H_0Ayy0)
- [LLM Agents](https://www.youtube.com/watch?v=Ub3GoFaUcds&list=PLoROMvodv4rOCXd21gf0CF4xr35yINeOy)

### Referências Técnicas
- Attention is All You Need: https://arxiv.org/abs/1706.03762
- OpenAI Embeddings Guide: https://platform.openai.com/docs/guides/embeddings

---

## Notas Gerais

### Boas Práticas
- Commit após cada milestone, não ao final da fase
- Documente decisões de design enquanto as toma
- Teste incrementalmente, não "no final"
- Se ficar preso >30min em um tópico, chame o Claude Code antes de pular — a estimativa revisada já conta com isso (era >2h no plano solo)

### Ajustes Esperados
Este PDI não é fixo. Você pode:
- Estender uma fase se precisar de mais profundidade
- Pular um tópico se já tiver conhecimento
- Adicionar recursos conforme descobre
- Mudar prioridades se projeto mudar

### Suporte & Colaboração
- Use Claude Code para automação de setup
- Crie slash commands para tarefas repetitivas
- Documente bloqueadores em `ISSUES.md`
- Refira-se a este PDI em commits: `feat(pdi): Fase 2 - Embeddings`

---

## Assinatura & Compromisso

**Desenvolvedor:** Thiago  
**Data de Criação:** 26/10/2026  
**Última Atualização:** 26/10/2026 (revisão das estimativas: 14h/semana + assistência)  

**Comprometimento:** Dedico 14h por semana para este PDI durante as próximas 7 semanas (banda realista: 7 a 9 semanas).

Assinatura: _______________

---

## Apêndice: Template de Nota de Aula

Para cada tópico concluído, use este template:

```markdown
# Tópico: [Nome]

## Objetivo
[Uma frase do que você quer aprender]

## Conceitos-Chave
- Conceito 1: [Explicação simples]
- Conceito 2: [Explicação simples]

## Implementação
[Código ou passos]

## Eureka Moment
[O que finalmente fez clicar?]

## Próximos Passos
[Como isso conecta ao próximo tópico?]

## Recursos Usados
- [Link 1]
- [Link 2]
```

---

**FIM DO DOCUMENTO**