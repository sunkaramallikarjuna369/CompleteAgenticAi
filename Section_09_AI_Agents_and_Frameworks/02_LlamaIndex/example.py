"""
LlamaIndex Framework
====================
Section 09

Demonstrates LlamaIndex concepts: indexing, querying,
and document retrieval.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math

print("=" * 60)
print("LLAMAINDEX CONCEPTS")
print("=" * 60)

class Document:
    def __init__(self, text, metadata=None):
        self.text = text
        self.metadata = metadata or {}

class Index:
    def __init__(self):
        self.documents = []
        self.nodes = []
    def add_document(self, doc):
        self.documents.append(doc)
        # Create nodes (chunks)
        words = doc.text.split()
        for i in range(0, len(words), 10):
            chunk = " ".join(words[i:i+10])
            self.nodes.append({"text": chunk, "doc_idx": len(self.documents)-1, "meta": doc.metadata})
    def query(self, query_text, top_k=3):
        q_words = set(query_text.lower().split())
        scored = []
        for node in self.nodes:
            n_words = set(node["text"].lower().split())
            score = len(q_words & n_words) / (len(q_words) + 1)
            scored.append((score, node))
        scored.sort(key=lambda x: -x[0])
        return scored[:top_k]

# Build index
index = Index()
index.add_document(Document("AI agents use tools and memory to solve complex tasks autonomously",
                            {"source": "agents.txt"}))
index.add_document(Document("RAG retrieves relevant documents to augment LLM generation with factual context",
                            {"source": "rag.txt"}))
index.add_document(Document("LlamaIndex provides data connectors and indexing for LLM applications",
                            {"source": "llamaindex.txt"}))

print(f"  Index: {len(index.documents)} docs, {len(index.nodes)} nodes")

# Query
results = index.query("How do agents use tools?", top_k=2)
print(f"\n  Query: 'How do agents use tools?'")
for score, node in results:
    print(f"    [{score:.2f}] {node['text'][:60]}... (from {node['meta'].get('source', 'N/A')})")

print("\nDone!")
