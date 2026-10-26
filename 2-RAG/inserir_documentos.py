import psycopg2
from sentence_transformers import SentenceTransformer

# Mesmo modelo multilíngue que escolhemos no item 2.1
modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

documentos = [
    "O cachorro correu no parque",
    "O cão brincou na praça",
    "O gato dormiu no sofá",
    "Preciso trocar o óleo do carro",
]

# Gera os embeddings de todos os documentos de uma vez
embeddings = modelo.encode(documentos)

# Conecta no PostgreSQL rodando no Docker
conexao = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="pdi_rag",
    user="postgres",
    password="pdi123"
)
cursor = conexao.cursor()

# Insere cada documento com seu respectivo embedding
for texto, vetor in zip(documentos, embeddings):
    cursor.execute(
        "INSERT INTO documentos (conteudo, embedding) VALUES (%s, %s)",
        (texto, vetor.tolist())  # converte o numpy array para lista comum
    )

conexao.commit()  # confirma as inserções no banco
cursor.close()
conexao.close()

print(f"{len(documentos)} documentos inseridos com sucesso!")