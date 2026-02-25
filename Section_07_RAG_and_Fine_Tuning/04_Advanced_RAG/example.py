"""
Advanced RAG
============
Section 07

Demonstrates advanced RAG: query rewriting,
hybrid search, and re-ranking.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("ADVANCED RAG TECHNIQUES")
print("=" * 60)

# 1. Query Rewriting
print("\n1. QUERY REWRITING")
print("-" * 40)

class QueryRewriter:
    def __init__(self):
        self.expansions = {
            "AI": ["artificial intelligence", "machine learning", "deep learning"],
            "LLM": ["large language model", "GPT", "transformer"],
            "RAG": ["retrieval augmented generation", "knowledge retrieval"],
        }
    def rewrite(self, query):
        words = query.split()
        expanded = []
        for w in words:
            if w.upper() in self.expansions:
                expanded.extend(self.expansions[w.upper()])
            expanded.append(w)
        return " ".join(expanded)
    def decompose(self, query):
        if " and " in query:
            parts = query.split(" and ")
            return [p.strip() for p in parts]
        return [query]

rewriter = QueryRewriter()
queries = ["How does RAG work?", "Explain AI and LLM architectures"]
for q in queries:
    print(f"  Original: {q}")
    print(f"  Expanded: {rewriter.rewrite(q)}")
    print(f"  Decomposed: {rewriter.decompose(q)}\n")

# 2. Hybrid Search (keyword + semantic)
print("2. HYBRID SEARCH")
print("-" * 40)

def keyword_score(query, doc):
    q_words = set(query.lower().split())
    d_words = set(doc.lower().split())
    return len(q_words & d_words) / (len(q_words) + 1)

def semantic_score(query_vec, doc_vec):
    dot = sum(a*b for a,b in zip(query_vec, doc_vec))
    na = math.sqrt(sum(a**2 for a in query_vec))
    nb = math.sqrt(sum(b**2 for b in doc_vec))
    return dot/(na*nb) if na and nb else 0

random.seed(42)
docs = [
    ("RAG improves accuracy by retrieving relevant documents", [0.9, 0.1, 0.3]),
    ("Vector databases store and search embeddings", [0.3, 0.8, 0.2]),
    ("Fine-tuning adapts models to specific domains", [0.2, 0.3, 0.9]),
]

query = "How does RAG retrieve documents?"
query_vec = [0.85, 0.15, 0.25]

print(f"  Query: {query}")
for doc_text, doc_vec in docs:
    ks = keyword_score(query, doc_text)
    ss = semantic_score(query_vec, doc_vec)
    hybrid = 0.4 * ks + 0.6 * ss
    print(f"  [{hybrid:.3f}] kw={ks:.2f} sem={ss:.2f} | {doc_text[:50]}...")

print("\nDone!")
