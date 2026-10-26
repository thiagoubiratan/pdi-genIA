# ============================================================
# chunking.py
# Objetivo: ler o PDF da LGPD e cortar o texto em pedaços (chunks)
# usando 4 estratégias, para comparar os resultados.
# A estratégia 4 (híbrida) é a que vamos usar de verdade no projeto.
# Rode de dentro da pasta 2-RAG:  python3 chunking.py
# ============================================================

import re                      # expressões regulares (busca e troca de padrões em texto)
from pypdf import PdfReader    # abre PDFs e extrai o texto


# ------------------------------------------------------------
# FUNÇÃO 1: decodificar
# O PDF da LGPD devolve as letras como "/uni0050" em vez de "P".
# Esta função troca cada código pela letra de verdade.
# ------------------------------------------------------------
def decodificar(texto):
    return re.sub(
        r"/uni([0-9A-Fa-f]{4})",                # procura "/uni" + 4 caracteres hexadecimais
        lambda m: chr(int(m.group(1), 16)),     # converte o código em letra (0050 -> 80 -> "P")
        texto
    )


# ------------------------------------------------------------
# FUNÇÃO 2: extrair_texto
# Abre o PDF, lê página por página e junta tudo em uma string só.
# ------------------------------------------------------------
def extrair_texto(caminho):
    leitor = PdfReader(caminho)                 # abre o arquivo PDF
    texto = ""                                  # começa com uma string vazia

    for pagina in leitor.pages:                 # percorre cada página
        texto_da_pagina = pagina.extract_text() # extrai o texto bruto da página
        texto += decodificar(texto_da_pagina)   # limpa os códigos /uniXXXX e acumula
        texto += "\n"                           # quebra de linha entre as páginas

    return texto


# ------------------------------------------------------------
# ESTRATÉGIA 1: chunk_tamanho_fixo
# Corta o texto a cada N caracteres, sem olhar o conteúdo.
# Defeito: pode cortar palavras e frases no meio.
# ------------------------------------------------------------
def chunk_tamanho_fixo(texto, tamanho):
    chunks = []

    # range(0, len(texto), tamanho) gera os pontos de início: 0, 400, 800, 1200...
    for inicio in range(0, len(texto), tamanho):
        fim = inicio + tamanho                  # onde este pedaço termina
        chunks.append(texto[inicio:fim])        # fatia do início até o fim

    return chunks


# ------------------------------------------------------------
# ESTRATÉGIA 2: chunk_com_overlap
# Tamanho fixo, mas cada chunk repete o final do anterior
# (a "sobreposição"), para que palavras/frases cortadas apareçam
# inteiras no chunk seguinte.
# ------------------------------------------------------------
def chunk_com_overlap(texto, tamanho, sobreposicao):
    chunks = []

    # O passo é quanto avançamos a cada corte.
    # Exemplo: tamanho=400 e sobreposicao=100 -> passo=300
    passo = tamanho - sobreposicao

    # Os pontos de início agora pulam de 300 em 300: 0, 300, 600, 900...
    for inicio in range(0, len(texto), passo):
        fim = inicio + tamanho                  # cada chunk continua com 400 caracteres
        chunks.append(texto[inicio:fim])

    return chunks


# ------------------------------------------------------------
# ESTRATÉGIA 3: chunk_por_artigo (semântica/estrutural)
# Corta o texto em cada início de artigo ("Art. 1º", "Art. 2º"...),
# respeitando a divisão natural da lei: um artigo = uma ideia.
# Defeito: alguns artigos são enormes e passam do limite do modelo.
# ------------------------------------------------------------
def chunk_por_artigo(texto):
    # O padrão r"\n(?=Art\. \d)" significa:
    #   \n            -> uma quebra de linha...
    #   (?=Art\. \d)  -> ...que seja seguida de "Art. " e um dígito.
    # O "(?=...)" olha à frente sem consumir o texto, então o "Art. 9º"
    # continua no início do chunk que ele abre.
    partes = re.split(r"\n(?=Art\. \d)", texto)

    # .strip() tira espaços e quebras de linha das pontas de cada parte.
    return [p.strip() for p in partes if p.strip()]


# ------------------------------------------------------------
# FUNÇÃO AUXILIAR: subdividir
# Divide um texto grande em pedaços de até "tamanho" caracteres,
# com sobreposição, cortando sempre num ESPAÇO (nunca no meio de
# uma palavra). Usada pela estratégia híbrida.
# ------------------------------------------------------------
def subdividir(texto, tamanho, sobreposicao):
    pedacos = []
    inicio = 0                                  # onde o pedaço atual começa

    while inicio < len(texto):
        # Limite máximo deste pedaço (sem passar do fim do texto)
        fim = min(inicio + tamanho, len(texto))

        # Se ainda não chegamos no fim do texto, procuramos o último espaço
        # dentro da janela para cortar ali e não partir uma palavra ao meio.
        if fim < len(texto):
            ultimo_espaco = texto.rfind(" ", inicio, fim)
            # Só usa esse espaço se ele estiver na segunda metade da janela
            # (evita gerar pedaços minúsculos)
            if ultimo_espaco > inicio + tamanho // 2:
                fim = ultimo_espaco

        pedacos.append(texto[inicio:fim].strip())   # guarda o pedaço

        if fim >= len(texto):                   # chegou no fim: acabou
            break

        # O próximo pedaço começa "sobreposicao" caracteres ANTES do fim
        # deste (é o overlap). O max(...) garante que sempre avançamos,
        # evitando um loop infinito.
        inicio = max(fim - sobreposicao, inicio + 1)

    return pedacos


# ------------------------------------------------------------
# ESTRATÉGIA 4: chunk_hibrido (artigo + subdivisão)
# 1) Corta por artigo.
# 2) Artigo pequeno: fica inteiro.
# 3) Artigo grande: é subdividido com overlap, e cada parte nova
#    ganha um rótulo "[Art. 5º, parte 2]" para manter o contexto.
# O cabeçalho da lei é descartado e os espaços duplicados são limpos.
# ------------------------------------------------------------
def chunk_hibrido(texto, tamanho_max=500, sobreposicao=100):
    # [1:] descarta o chunk 0 (o cabeçalho, que não tem conteúdo útil)
    artigos = chunk_por_artigo(texto)[1:]

    chunks = []
    for artigo in artigos:
        # Troca qualquer sequência de espaços/quebras de linha por um
        # único espaço (limpa os espaços duplicados que vêm do PDF)
        artigo = re.sub(r"\s+", " ", artigo).strip()

        # Artigo que cabe no limite: vira um chunk inteiro
        if len(artigo) <= tamanho_max:
            chunks.append(artigo)
            continue                            # passa para o próximo artigo

        # Artigo grande: descobre o rótulo ("Art. 5º", "Art. 55-A"...)
        rotulo = re.match(r"Art\. \d+\S*", artigo).group(0)

        # Subdivide o artigo em pedaços com overlap
        partes = subdividir(artigo, tamanho_max, sobreposicao)

        for n, parte in enumerate(partes, start=1):
            if n == 1:
                chunks.append(parte)            # a parte 1 já começa com "Art. X"
            else:
                # As demais ganham o rótulo, para não perderem a origem
                chunks.append(f"[{rotulo}, parte {n}] {parte}")

    return chunks


# ------------------------------------------------------------
# FUNÇÃO AUXILIAR: mostrar_estatisticas
# Imprime quantos chunks foram gerados e como estão os tamanhos.
# ------------------------------------------------------------
def mostrar_estatisticas(nome, chunks):
    tamanhos = [len(c) for c in chunks]         # lista com o tamanho de cada chunk

    print(f"=== {nome} ===")
    print(f"Total de chunks:              {len(chunks)}")
    print(f"Menor chunk:                  {min(tamanhos)} caracteres")
    print(f"Maior chunk:                  {max(tamanhos)} caracteres")
    print(f"Média:                        {sum(tamanhos) // len(tamanhos)} caracteres")
    print(f"Chunks acima de 1000 caract.: {len([t for t in tamanhos if t > 1000])}")
    print()


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

# 1) Extrai o texto do PDF (caminho relativo à pasta 2-RAG)
texto = extrair_texto("docs/lgpd.pdf")

# 2) Aplica as 4 estratégias ao mesmo texto
chunks_fixo = chunk_tamanho_fixo(texto, 400)
chunks_overlap = chunk_com_overlap(texto, 400, 100)
chunks_artigo = chunk_por_artigo(texto)
chunks_hibrido = chunk_hibrido(texto, 500, 100)

# 3) Compara os números das 4 estratégias
mostrar_estatisticas("Estratégia 1: tamanho fixo (400)", chunks_fixo)
mostrar_estatisticas("Estratégia 2: overlap (400 com 100)", chunks_overlap)
mostrar_estatisticas("Estratégia 3: por artigo", chunks_artigo)
mostrar_estatisticas("Estratégia 4: híbrida (artigo + subdivisão)", chunks_hibrido)

# 4) Mostra um exemplo de artigo subdividido: o primeiro chunk que
#    começa com "[Art." (uma "parte 2"), junto com o final do chunk
#    anterior, para você ver a sobreposição e o rótulo.
posicao = next(i for i, c in enumerate(chunks_hibrido) if c.startswith("[Art."))

print("--- FINAL do chunk anterior (últimos 150 caracteres) ---")
print(chunks_hibrido[posicao - 1][-150:])
print()
print(f"--- CHUNK {posicao} (começa com o rótulo) ---")
print(chunks_hibrido[posicao])