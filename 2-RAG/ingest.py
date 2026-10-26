# ============================================================
# ingest.py
# Pipeline completo de ingestão:
#   PDF -> texto -> chunks -> embeddings -> pgVector
# Uso (de dentro da pasta 2-RAG):
#   python3 ingest.py docs/lgpd.pdf
# ============================================================

import re  # expressões regulares
import sys  # acesso aos argumentos da linha de comando

import psycopg2  # conexão com o PostgreSQL
from pypdf import PdfReader  # leitura de PDF
from sentence_transformers import SentenceTransformer  # modelo de embeddings

# ------------------------------------------------------------
# CONFIGURAÇÕES (tudo que pode mudar fica aqui no topo)
# ------------------------------------------------------------
MODELO = "paraphrase-multilingual-MiniLM-L12-v2"   # o modelo que escolhemos no item 2.1
TABELA = "chunks_lgpd"                              # tabela criada para a LGPD
TAMANHO_MAX = 500                                   # tamanho máximo de um chunk (em caracteres)
SOBREPOSICAO = 100                                  # overlap entre partes de um artigo grande

CONEXAO_BANCO = {
    "host": "localhost",
    "port": 5432,
    "dbname": "pdi_rag",
    "user": "postgres",
    "password": "pdi123",
}


# ------------------------------------------------------------
# ETAPA 1: PDF -> texto
# ------------------------------------------------------------
def decodificar(texto):
    # Troca "/uni0050" pela letra "P" (o PDF da LGPD devolve as letras assim)
    return re.sub(
        r"/uni([0-9A-Fa-f]{4})",
        lambda m: chr(int(m.group(1), 16)),
        texto
    )


def extrair_texto(caminho):
    leitor = PdfReader(caminho)
    texto = ""
    for pagina in leitor.pages:
        texto += decodificar(pagina.extract_text()) + "\n"
    return texto


# ------------------------------------------------------------
# ETAPA 2: texto -> chunks (estratégia híbrida: artigo + subdivisão)
# ------------------------------------------------------------
def chunk_por_artigo(texto):
    # Corta em cada quebra de linha seguida de "Art. " e um dígito
    partes = re.split(r"\n(?=Art\. \d)", texto)
    return [p.strip() for p in partes if p.strip()]


def subdividir(texto, tamanho, sobreposicao):
    # Divide um texto grande em pedaços com overlap, cortando sempre num espaço
    pedacos = []
    inicio = 0

    while inicio < len(texto):
        fim = min(inicio + tamanho, len(texto))

        if fim < len(texto):
            ultimo_espaco = texto.rfind(" ", inicio, fim)
            if ultimo_espaco > inicio + tamanho // 2:
                fim = ultimo_espaco

        pedacos.append(texto[inicio:fim].strip())

        if fim >= len(texto):
            break

        inicio = max(fim - sobreposicao, inicio + 1)

    return pedacos


def chunk_hibrido(texto, tamanho_max, sobreposicao):
    artigos = chunk_por_artigo(texto)[1:]        # [1:] descarta o cabeçalho da lei

    chunks = []
    for artigo in artigos:
        artigo = re.sub(r"\s+", " ", artigo).strip()    # limpa espaços duplicados

        if len(artigo) <= tamanho_max:
            chunks.append(artigo)                # artigo pequeno: chunk inteiro
            continue

        rotulo = re.match(r"Art\. \d+\S*", artigo).group(0)   # ex: "Art. 5º"
        partes = subdividir(artigo, tamanho_max, sobreposicao)

        for n, parte in enumerate(partes, start=1):
            if n == 1:
                chunks.append(parte)
            else:
                chunks.append(f"[{rotulo}, parte {n}] {parte}")

    return chunks


# ------------------------------------------------------------
# ETAPA 3: chunks -> embeddings
# ------------------------------------------------------------
def gerar_embeddings(chunks):
    print(f"Carregando o modelo {MODELO}...")
    modelo = SentenceTransformer(MODELO)

    # max_seq_length é o limite de tokens que o modelo lê por entrada
    print(f"Limite do modelo: {modelo.max_seq_length} tokens por chunk")

    print(f"Gerando embeddings de {len(chunks)} chunks...")
    # encode aceita a lista inteira de uma vez e processa em lotes
    return modelo.encode(chunks, show_progress_bar=True)


# ------------------------------------------------------------
# ETAPA 4: embeddings -> pgVector
# ------------------------------------------------------------
def inserir_no_banco(chunks, embeddings):
    conexao = psycopg2.connect(**CONEXAO_BANCO)   # ** abre o dicionário como argumentos
    cursor = conexao.cursor()

    # Esvazia a tabela antes de inserir. Sem isso, rodar o script duas vezes
    # duplicaria todos os chunks. RESTART IDENTITY reinicia o id em 1.
    cursor.execute(f"TRUNCATE TABLE {TABELA} RESTART IDENTITY")

    for texto, vetor in zip(chunks, embeddings):
        cursor.execute(
            f"INSERT INTO {TABELA} (conteudo, embedding) VALUES (%s, %s)",
            (texto, vetor.tolist())               # tolist converte o array numpy em lista comum
        )

    conexao.commit()                              # confirma TUDO de uma vez (uma transação só)

    # Conta quantas linhas ficaram na tabela para conferir
    cursor.execute(f"SELECT COUNT(*) FROM {TABELA}")
    total = cursor.fetchone()[0]

    cursor.close()
    conexao.close()
    return total


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL: junta as 4 etapas
# ------------------------------------------------------------
if __name__ == "__main__":
    # sys.argv[1] é o primeiro argumento depois do nome do script.
    # Se você não passar nenhum, usa "docs/lgpd.pdf" como padrão.
    caminho_pdf = sys.argv[1] if len(sys.argv) > 1 else "docs/lgpd.pdf"

    print(f"1) Lendo o PDF: {caminho_pdf}")
    texto = extrair_texto(caminho_pdf)
    print(f"   {len(texto)} caracteres extraídos\n")

    print("2) Gerando chunks (estratégia híbrida)")
    chunks = chunk_hibrido(texto, TAMANHO_MAX, SOBREPOSICAO)
    print(f"   {len(chunks)} chunks gerados\n")

    print("3) Gerando embeddings")
    embeddings = gerar_embeddings(chunks)
    print()

    print("4) Inserindo no banco")
    total = inserir_no_banco(chunks, embeddings)
    print(f"   {total} linhas na tabela {TABELA}\n")

    print("Ingestão concluída!")