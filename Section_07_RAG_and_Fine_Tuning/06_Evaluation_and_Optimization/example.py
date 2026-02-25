"""
Evaluation and Optimization
===========================
Section 07

Demonstrates RAG evaluation: relevance scoring,
faithfulness checking, and optimization.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("RAG EVALUATION & OPTIMIZATION")
print("=" * 60)

# 1. Relevance Scoring
print("\n1. RELEVANCE SCORING")
print("-" * 40)

def relevance_score(query, document):
    q_words = set(query.lower().split())
    d_words = set(document.lower().split())
    if not q_words:
        return 0
    return len(q_words & d_words) / len(q_words)

query = "How do agents use tools for planning?"
docs = [
    "Agents use tools to interact with external systems and plan tasks",
    "Machine learning models learn patterns from data",
    "Planning and tool use are core capabilities of AI agents",
    "The weather forecast predicts sunny skies tomorrow",
]

print(f"  Query: {query}")
for doc in docs:
    score = relevance_score(query, doc)
    label = "RELEVANT" if score > 0.3 else "NOT RELEVANT"
    print(f"  [{score:.2f} {label:13s}] {doc[:55]}...")

# 2. Faithfulness Check
print("\n2. FAITHFULNESS CHECK")
print("-" * 40)

def check_faithfulness(answer, context):
    answer_claims = set(answer.lower().split())
    context_words = set(context.lower().split())
    overlap = len(answer_claims & context_words)
    return overlap / len(answer_claims) if answer_claims else 0

context = "RAG retrieves relevant documents and uses them to generate accurate responses"
answers = [
    "RAG generates accurate responses using retrieved documents",
    "RAG uses quantum computing to process neural networks",
]

for ans in answers:
    score = check_faithfulness(ans, context)
    status = "FAITHFUL" if score > 0.4 else "UNFAITHFUL"
    print(f"  [{status:11s} {score:.2f}] {ans}")

# 3. Optimization metrics
print("\n3. OPTIMIZATION COMPARISON")
print("-" * 40)

random.seed(42)
configs = [
    ("Baseline", {"chunk_size": 200, "top_k": 3}),
    ("Larger chunks", {"chunk_size": 500, "top_k": 3}),
    ("More results", {"chunk_size": 200, "top_k": 5}),
    ("Hybrid search", {"chunk_size": 200, "top_k": 3}),
]

print(f"  {'Config':15s} {'Relevance':>10} {'Latency':>10} {'Cost':>8}")
for name, cfg in configs:
    rel = 0.6 + random.random() * 0.35
    lat = 100 + random.random() * 400
    cost = 0.001 + random.random() * 0.01
    print(f"  {name:15s} {rel:>10.3f} {lat:>9.0f}ms ${cost:>7.4f}")

print("\nDone!")
