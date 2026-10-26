import psycopg2
from sentence_transformers import SentenceTransformer

# Mesmo modelo usado para inserir os documentos
modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# A pergunta/busca do usuário
pergunta = "Meu cachorro gosta de passear"

# Gera o embedding da pergunta
embedding_pergunta = modelo.encode(pergunta).tolist()

# Conecta no banco
conexao = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="pdi_rag",
    user="postgres",
    password="pdi123"
)
cursor = conexao.cursor()

# Busca os documentos mais PARECIDOS (menor distância de cosseno)
cursor.execute(
    """
    SELECT conteudo, embedding <=> %s::vector AS distancia
    FROM documentos
    ORDER BY distancia ASC
    LIMIT 3
    """,
    (embedding_pergunta,)
)

resultados = cursor.fetchall()

print(f'Pergunta: "{pergunta}"\n')
print("Documentos mais parecidos:")
for conteudo, distancia in resultados:
    print(f'  → "{conteudo}" (distância: {distancia:.4f})')

cursor.close()
conexao.close()