from sentence_transformers import SentenceTransformer
import faiss
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = []

for f in os.listdir("../data/flood_docs"):
    with open(f"../data/flood_docs/{f}", "r", encoding="utf-8") as file:
        docs.append(file.read())

embeddings = model.encode(docs)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)


def get_context(query):
    q = model.encode([query])
    _, idx = index.search(q, 2)

    return "\n".join([docs[i] for i in idx[0]])