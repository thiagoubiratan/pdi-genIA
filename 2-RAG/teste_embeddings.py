# usando o modelo all-MiniLM-L6-v2

from numpy import dot
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer

# Modelo pequeno e rápido, ótimo para começar
modelo = SentenceTransformer('all-MiniLM-L6-v2')

frases = [
    "O cachorro correu no parque",
    "O cão brincou na praça",
    "O gato dormiu no sofá",
    "Preciso trocar o óleo do carro",
]

# Gera os embeddings (vetores) para cada frase
embeddings = modelo.encode(frases)

print(f"Dimensão de cada vetor: {embeddings[0].shape}")
print()

def cosine_similarity(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))

# Compara a primeira frase com todas as outras
for i in range(1, len(frases)):
    sim = cosine_similarity(embeddings[0], embeddings[i])
    print(f'"{frases[0]}" vs "{frases[i]}" → similaridade: {sim:.4f}')