"""
Vector Databases
================
Section 07

Demonstrates vector DB concepts: embeddings,
similarity search, and indexing.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("VECTOR DATABASES")
print("=" * 60)

class VectorDB:
    def __init__(self, dim):
        self.dim = dim
        self.vectors = {}
        self.metadata = {}

    def insert(self, doc_id, vector, meta=None):
        self.vectors[doc_id] = vector
        self.metadata[doc_id] = meta or {}

    def cosine_sim(self, a, b):
        dot = sum(x*y for x,y in zip(a,b))
        na = math.sqrt(sum(x**2 for x in a))
        nb = math.sqrt(sum(x**2 for x in b))
        return dot/(na*nb) if na and nb else 0

    def search(self, query, top_k=3):
        results = []
        for doc_id, vec in self.vectors.items():
            sim = self.cosine_sim(query, vec)
            results.append((doc_id, sim, self.metadata.get(doc_id, {})))
        results.sort(key=lambda x: -x[1])
        return results[:top_k]

random.seed(42)
db = VectorDB(dim=4)

docs = [
    ("doc1", [0.9, 0.1, 0.2, 0.3], {"topic": "AI"}),
    ("doc2", [0.8, 0.2, 0.1, 0.4], {"topic": "AI"}),
    ("doc3", [0.1, 0.9, 0.3, 0.2], {"topic": "web"}),
    ("doc4", [0.2, 0.8, 0.4, 0.1], {"topic": "web"}),
    ("doc5", [0.5, 0.5, 0.8, 0.1], {"topic": "data"}),
]
for did, vec, meta in docs:
    db.insert(did, vec, meta)

query = [0.85, 0.15, 0.2, 0.35]
results = db.search(query, top_k=3)

print(f"  Database: {len(db.vectors)} documents, {db.dim} dimensions")
print(f"\n  Search results:")
for doc_id, sim, meta in results:
    print(f"    {doc_id}: similarity={sim:.3f}, topic={meta.get('topic', 'N/A')}")

print("\nDone!")
