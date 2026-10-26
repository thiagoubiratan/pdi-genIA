# PDI - Desenvolvimento em GenAI & Agentes

**Data de início:** 26/10/2026  
**Data estimada de conclusão:** 04/01/2027 a 01/02/2027 (10-14 semanas)  
**Objetivo geral:** Dominar arquitetura de agentes GenAI com RAG, implementar sistema de produção capaz de processar e recuperar informações de PDFs com segurança e eficiência.

---

## Resumo Executivo

| Fase | Duração | Foco | Status |
|------|---------|------|--------|
| 1: Fundamentos | 2-3 sem | Python, Streamlit, Prompt Eng | ⏳ Não iniciado |
| 2: RAG | 2-3 sem | Embeddings, Vector DB, Indexação | ⏳ Não iniciado |
| 3: Agentes | 3-4 sem | LLM Params, LangChain, Guardrails | ⏳ Não iniciado |
| 4: Capstone | 2-3 sem | Projeto integrado (Agente PDF) | ⏳ Não iniciado |

**Tempo total estimado:** 100-130 horas (5-8h/semana por ~16 semanas)

---

## FASE 1: Fundamentos (2-3 semanas)

**Objetivo:** Construir base sólida em Python, redes neurais e prompt engineering para compreender o que vem depois.

### 1.1 Python + Streamlit

**Data de início:** 26/10/2026

**Descrição:** Dominar o essencial de Python para dados e criar UIs de prototipagem rápida.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Setup ambiente Python | ⏳ | [Streamlit Docs](https://docs.streamlit.io) | Venv + requirements.txt | 0.5h |
| Bloco 1 — Base Python | ⏳ | Documentação + prática | Exercícios com variáveis, tipos, condicionais, loops, funções e imports | 2h |
| Bloco 2 — Python específico | ⏳ | Documentação + prática | Exercícios com list comprehensions, lambda, arquivos, try/except e f-strings | 3h |
| Bloco 3 — Python avançado | ⏳ | Documentação + prática | Exercícios com classes, decorators, async/await e tipagem com Pydantic | 4h |
| Introdução Streamlit | ⏳ | [Getting Started](https://docs.streamlit.io/get-started) | App com 3 widgets (input, slider, button) | 2h |
| App interativo básico | ⏳ | [Streamlit Docs](https://docs.streamlit.io) | Calculadora com estado | 2h |

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
| Princípios de prompting | ⏳ | [Claude Prompt Engineering Guide](https://platform.claude.com/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Checklist: clareza, contexto, estrutura | 2h |
| Few-shot examples | ⏳ | Documentação + prática | Teste de classificação de sentimento com exemplos | 2h |
| Prompt caching | ⏳ | Documentação Anthropic | Entendimento de cache_control (ephemeral), custo e latência | 1h |
| Chain-of-thought | ⏳ | Documentação + experimentação | Comparação com vs sem CoT, trade-off de tokens de output | 2h |
| Coleta de prompts efetivos | ⏳ | Seu acervo | `prompts_collection.md` com exemplos categorizados (estruturação, few-shot, CoT, caching) | 2h |

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

**Conclusão da Fase 1:** Data estimada: _________ | Data real: _________

---

## FASE 2: RAG (Retrieval-Augmented Generation)

**Objetivo:** Implementar pipeline completo de indexação e recuperação de informações com vector databases.

### 2.1 Embeddings & Modelos

**Descrição:** Entender como textos são convertidos em vetores e quais modelos usar.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| O que são embeddings | ⏳ | [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings) | Documento: dimensionality, cosine similarity, use cases | 2h |
| Testar modelos | ⏳ | Hugging Face + OpenAI + código próprio | Comparação: 3 modelos (OpenAI, sentence-transformers, open-source) | 4h |
| Comparar resultados | ⏳ | Notebooks | Tabela: speed, dimensão, qualidade, custo | 2h |

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
| Setup PostgreSQL local | ⏳ | Docker ou instalação nativa | PostgreSQL rodando na porta 5432 | 1h |
| Instalação pgVector | ⏳ | [pgVector GitHub](https://github.com/pgvector/pgvector) | Extensão instalada e criada | 1h |
| Schema básico | ⏳ | SQL + documentação | Tabela com colunas: id, content, embedding (vector) | 1h |
| Queries básicas | ⏳ | Experimentação | Scripts: INSERT, cosine similarity search | 2h |
| Índices para performance | ⏳ | pgVector docs | HNSW ou IVFFlat index criado | 2h |

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
| Leitura de PDF | ⏳ | PyPDF2 ou pdfplumber | Script que extrai texto de PDF | 1h |
| Chunking estratégias | ⏳ | LangChain docs + experimentação | 3 estratégias testadas (fixed size, semantic, overlap) | 3h |
| Geração de embeddings | ⏳ | Seu código | Script que chama API de embeddings | 2h |
| Inserção em pgVector | ⏳ | psycopg2 ou SQLAlchemy | Inserir batch de embeddings | 2h |
| Pipeline integrado | ⏳ | Seu código | Script: `python ingest.py docs/sample.pdf` → pgVector | 3h |

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
| Busca por similaridade | ⏳ | pgVector + Python | Query base: `ORDER BY embedding <-> query_embedding LIMIT 5` | 1h |
| BM25 (hybrid search) | ⏳ | Implementação + documentação | Combinar keyword search + vector search | 3h |
| Reranking | ⏳ | Biblioteca como `rank-bm25` | Reordenar top-k resultados por relevância | 2h |
| Avaliação de qualidade | ⏳ | Teste manual + métricas | Documento comparando 3 estratégias em 5 queries | 3h |

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
| Conceitos Graph RAG | ⏳ | [Seu vídeo](https://www.youtube.com/watch?v=_HQ2H_0Ayy0) | Notas: entities, relationships, queries | 2h |
| Comparação Vector vs Graph | ⏳ | Pesquisa própria | Documento: quando usar cada, trade-offs | 2h |
| Experimento básico | ⏳ | Neo4j ou equivalente (opcional) | Prototipo simples comparando resultados | 2h |

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

**Conclusão da Fase 2:** Data estimada: _________ | Data real: _________

---

## FASE 3: Agentes & LLM Orchestration - (MCP)

**Objetivo:** Orquestrar chamadas a LLMs com estado, memória e raciocínio multi-turno.

### 3.1 Parâmetros de LLM

**Descrição:** Dominar como tunar temperatura, top-p, max_tokens para diferentes casos de uso.

| Item | Status | Recurso | Entregável | Tempo Est. |
|------|--------|---------|-----------|-----------|
| Temperature & Randomness | ⏳ | Claude API docs + experimentação | Documento: T=0 vs T=1, casos de uso | 2h |
| Top-p, Top-k, Frequency Penalty | ⏳ | Claude API docs | Documento explicando cada parâmetro | 2h |
| Max_tokens & stopping | ⏳ | Experiência | Guidelines para seu projeto | 1h |
| Testes comparativos | ⏳ | Script de testes | 5 prompts com 3 configs diferentes, comparar resultados | 3h |

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
| Setup LangChain | ⏳ | [LangChain Docs](https://docs.langchain.com) | Projeto base estruturado | 1h |
| LLMChain simples | ⏳ | Tutorial official | Chain: input → LLM → output | 2h |
| PromptTemplate | ⏳ | Docs + código | 3 templates para diferentes tarefas | 2h |
| Chain com memória | ⏳ | LangChain Memory docs | Chain que mantém histórico conversacional | 3h |
| Chain com tools | ⏳ | LangChain Tools docs | Chain que chama função Python (ex: cálculo) | 3h |

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
| Conceito de State Machines | ⏳ | LangGraph docs | Documento: estados, transitions | 2h |
| Primeiro graph simples | ⏳ | Documentação official | Agent com 2-3 estados rodando | 4h |
| Action nodes | ⏳ | Docs + código | Nodes que executam ações (tools) | 3h |
| Loops e condicionals | ⏳ | Experimentação | Agent que decide iterar ou parar | 3h |
| Visualização de graphs | ⏳ | LangGraph viz tools | Diagrama dos states funcionando | 2h |

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
| Input validation | ⏳ | Pydantic + custom logic | Middleware que rejeita inputs malformados | 2h |
| Output filtering | ⏳ | Regex + classification | Verificar se resposta sai do escopo | 2h |
| Rate limiting | ⏳ | Biblioteca ou custom | Middleware que limita requisições | 2h |
| Injection prevention | ⏳ | Documentação + código | Proteção contra prompt injection | 2h |
| Logging & monitoring | ⏳ | Estrutura de logs | Registrar todas as requisições/respostas | 2h |

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
| Short-term (conversa) | ⏳ | LangChain ConversationBufferMemory | Janela deslizante de mensagens | 2h |
| Long-term (embeddings) | ⏳ | Vector similarity + metadata | Recuperar contexto anterior relevante | 3h |
| Resumo automático | ⏳ | LLM para criar resumos | Sumarizar conversa antes de esquecer | 2h |
| Teste integrado | ⏳ | Script multi-turno | Conversa que referencia tópicos antigos | 3h |

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
| O que é MCP e por que importa | ⏳ | [MCP Docs](https://modelcontextprotocol.io/introduction) | Documento: arquitetura host/client/server, casos de uso | 2h |
| Componentes do protocolo | ⏳ | Documentação oficial | Diagrama: Tools, Resources, Prompts e como interagem | 2h |
| Criar MCP Server simples | ⏳ | SDK Python (`mcp`) | Server com 1-2 tools expostas (ex: busca em arquivo local) | 4h |
| Conectar agent ao MCP Server | ⏳ | Claude API + MCP | Agent que descobre e invoca tools via protocolo | 4h |
| MCP com múltiplos servidores | ⏳ | Experimentação | Agent consumindo 2 servidores distintos simultaneamente | 3h |
| Segurança e controle de acesso | ⏳ | MCP Docs + código | Validação de permissões e escopos no servidor | 2h |

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

**Conclusão da Fase 3:** Data estimada: _________ | Data real: _________

---

## FASE 4: Capstone - Agente PDF com RAG

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

**Sprint 1: Backend Base**
- [ ] Estrutura de pastas criada
- [ ] Config + logger setup
- [ ] PDF loader funcionando
- [ ] Chunking com 3 estratégias
- [ ] Embedder conectado a modelo escolhido

**Sprint 2: Vector Store**
- [ ] Migrations de schema rodam
- [ ] Inserção de embeddings funciona
- [ ] Retriever retorna top-k relevantes
- [ ] Reranking implementado
- [ ] Testes: retrieval@5, retrieval@10

**Sprint 3: Agent**
- [ ] Tools definidas (search, summary)
- [ ] LangGraph state machine criada
- [ ] Agent consegue chamar tools
- [ ] Memória implementada
- [ ] Guardrails bloqueando inputs inválidos

**Sprint 4: UI + Integração**
- [ ] Streamlit app com upload
- [ ] Chat interface para perguntas
- [ ] Exibição de chunks recuperados
- [ ] Histórico de conversa
- [ ] Tratamento de erros robusto

**Sprint 5: Testes + Docs**
- [ ] Testes unitários (>80% coverage)
- [ ] Testes de integração (3 cenários)
- [ ] README com instruções
- [ ] Documentação de arquitetura
- [ ] Exemplos de prompts

### 4.4 Casos de Uso para Teste

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

**Conclusão da Fase 4:** Data estimada: _________ | Data real: _________

---

## Rastreamento Geral de Progresso

### Timeline Visual

```
┌─ Semana 1-3: Fundamentos ────┐
│  ⏳ Python
│  ⏳ Prompting
│
├─ Semana 4-6: RAG ────────────┐
│  ⏳ Embeddings
│  ⏳ pgVector
│  ⏳ Indexação
│  ⏳ Retrieval
│
├─ Semana 7-10: Agents ────────┐
│  ⏳ LLM Params
│  ⏳ LangChain
│  ⏳ LangGraph
│  ⏳ Guardrails
│  ⏳ Memory
│  ⏳ MCP
│
└─ Semana 11-14: Capstone ─────┐
   ⏳ Integração completa
   ⏳ Testes
   ⏳ Documentação
   ⏳ Deploy ready
```

### Horas por Semana

| Semana | Fase | Horas Planejadas | Horas Reais | Notas |
|--------|------|-----------------|-----------|-------|
| 1 | Fund. | 6h | - | |
| 2 | Fund. | 6h | - | |
| 3 | Fund. | 6h | - | |
| 4 | RAG | 7h | - | |
| 5 | RAG | 7h | - | |
| 6 | RAG | 7h | - | |
| 7 | Agent | 8h | - | |
| 8 | Agent | 8h | - | |
| 9 | Agent | 8h | - | |
| 10 | Agent | 8h | - | |
| 11 | Capstone | 8h | - | |
| 12 | Capstone | 8h | - | |
| 13 | Capstone | 8h | - | |
| 14 | Capstone | 6h | - | |

**Total planejado:** 115h | **Total realizado:** ___h

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
- Se ficar preso >2h em um tópico, ajuste ou pule para próximo

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
**Data de Criação:** _____________  
**Última Atualização:** _____________  

**Comprometimento:** Dedico 5-8h por semana para este PDI durante os próximos 14 semanas.

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