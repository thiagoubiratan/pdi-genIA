# usando o modelo paraphrase-multilingual-MiniLM-L12-v2

from numpy import dot
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer


def cosine_similarity(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))

frases = [
    "O cachorro correu no parque",
    "O cão brincou na praça",
    "O gato dormiu no sofá",
    "Preciso trocar o óleo do carro",
]

modelos = {
    "all-MiniLM-L6-v2 (inglês)": "all-MiniLM-L6-v2",
    "paraphrase-multilingual-MiniLM-L12-v2 (multilíngue)": "paraphrase-multilingual-MiniLM-L12-v2",
}

for nome, modelo_id in modelos.items():
    print(f"\n{'='*60}")
    print(f"Modelo: {nome}")
    print('='*60)

    modelo = SentenceTransformer(modelo_id)
    embeddings = modelo.encode(frases)

    print(f"Dimensão de cada vetor: {embeddings[0].shape}\n")

    for i in range(1, len(frases)):
        sim = cosine_similarity(embeddings[0], embeddings[i])
        print(f'"{frases[0]}" vs "{frases[i]}" → similaridade: {sim:.4f}')