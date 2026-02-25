"""
RAG Fundamentals
================
Section 07

Demonstrates RAG pipeline: document chunking,
retrieval, and augmented generation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math
from collections import Counter

print("=" * 60)
print("RAG FUNDAMENTALS")
print("=" * 60)

class SimpleRAG:
    def __init__(self):
        self.documents = []

    def add_document(self, text, metadata=None):
        words = set(text.lower().split())
        self.documents.append({"text": text, "words": words, "meta": metadata or {}})

    def retrieve(self, query, top_k=3):
        query_words = set(query.lower().split())
        scored = []
        for doc in self.documents:
            overlap = len(query_words & doc["words"])
            score = overlap / (len(query_words) + 1)
            scored.append((score, doc))
        scored.sort(key=lambda x: -x[0])
        return scored[:top_k]

    def generate_prompt(self, query, context_docs):
        context = "\n".join(f"- {doc['text'][:100]}" for _, doc in context_docs)
        return f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"

rag = SimpleRAG()
rag.add_document("Python is a popular programming language for AI and machine learning")
rag.add_document("LangChain is a framework for building LLM-powered applications")
rag.add_document("RAG combines retrieval with generation for better accuracy")
rag.add_document("Vector databases store embeddings for similarity search")
rag.add_document("Fine-tuning adapts pre-trained models to specific tasks")

query = "How does RAG improve accuracy?"
results = rag.retrieve(query, top_k=3)

print(f"  Query: {query}")
print(f"\n  Retrieved documents:")
for score, doc in results:
    print(f"    [{score:.2f}] {doc['text'][:70]}...")

prompt = rag.generate_prompt(query, results)
print(f"\n  Generated prompt ({len(prompt)} chars):")
print(f"  {prompt[:200]}")

print("\nDone!")
