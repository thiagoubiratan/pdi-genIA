# ============================================================
# buscar_lgpd.py
# Faz perguntas em linguagem natural e busca no pgVector os
# chunks da LGPD semanticamente mais parecidos.
# Uso (de dentro da pasta 2-RAG):
#   python3 buscar_lgpd.py                      (usa 3 perguntas de teste)
#   python3 buscar_lgpd.py "sua pergunta aqui"  (usa a sua pergunta)
# ============================================================

import sys                                       # argumentos da linha de comando
import psycopg2                                  # conexão com o PostgreSQL
from sentence_transformers import SentenceTransformer   # modelo de embeddings

MODELO = "paraphrase-multilingual-MiniLM-L12-v2"   # TEM que ser o mesmo modelo da ingestão
TABELA = "chunks_lgpd"
RESULTADOS = 3                                      # quantos chunks trazer por pergunta

CONEXAO_BANCO = {
    "host": "localhost",
    "port": 5432,
    "dbname": "pdi_rag",
    "user": "postgres",
    "password": "pdi123",
}

PERGUNTAS_TESTE = [
    "Quais são os direitos do titular dos dados?",
    "O que é consentimento?",
    "Quando o tratamento de dados pessoais pode ser feito sem consentimento?",
]


def buscar(cursor, modelo, pergunta):
    # Transforma a pergunta em vetor, com o MESMO modelo usado nos chunks
    vetor = modelo.encode(pergunta).tolist()

    # <=> é a distância de cosseno do pgVector (menor = mais parecido)
    cursor.execute(
        f"""
        SELECT conteudo, embedding <=> %s::vector AS distancia
        FROM {TABELA}
        ORDER BY distancia ASC
        LIMIT {RESULTADOS}
        """,
        (vetor,)
    )
    return cursor.fetchall()


if __name__ == "__main__":
    # Se você passou uma pergunta no terminal, usa ela; senão, usa as de teste
    perguntas = [sys.argv[1]] if len(sys.argv) > 1 else PERGUNTAS_TESTE

    modelo = SentenceTransformer(MODELO)
    conexao = psycopg2.connect(**CONEXAO_BANCO)
    cursor = conexao.cursor()

    for pergunta in perguntas:
        print("=" * 70)
        print(f"PERGUNTA: {pergunta}")
        print("=" * 70)

        for posicao, (conteudo, distancia) in enumerate(buscar(cursor, modelo, pergunta), start=1):
            print(f"\n#{posicao}  (distância: {distancia:.4f})")
            print(conteudo[:300])                 # mostra só os 300 primeiros caracteres
        print()

    cursor.close()
    conexao.close()