"""
Natural Language Processing
===========================
Section 02

Demonstrates NLP basics: tokenization, BoW,
TF-IDF, and cosine similarity.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, re
from collections import Counter

print("=" * 60)
print("1. TOKENIZATION")
print("=" * 60)

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

text = "AI agents use large language models for reasoning and planning."
tokens = tokenize(text)
print(f"  Text: {text}")
print(f"  Tokens ({len(tokens)}): {tokens}")

print("\n" + "=" * 60)
print("2. BAG OF WORDS & TF-IDF")
print("=" * 60)

docs = [
    "AI agents are autonomous systems",
    "Machine learning models learn from data",
    "AI systems use machine learning models",
]
tokenized = [tokenize(d) for d in docs]
vocab = sorted(set(w for t in tokenized for w in t))

print("  BoW Matrix:")
bow = []
for i, toks in enumerate(tokenized):
    counts = Counter(toks)
    vec = [counts.get(w, 0) for w in vocab]
    bow.append(vec)
    print(f"    Doc {i}: {vec[:8]}...")

# TF-IDF
n_docs = len(docs)
idf = []
for w in vocab:
    df = sum(1 for toks in tokenized if w in toks)
    idf.append(math.log(n_docs / df))

tfidf = []
for vec in bow:
    tfidf_vec = [tf * idf_val for tf, idf_val in zip(vec, idf)]
    tfidf.append(tfidf_vec)

def cosine_sim(a, b):
    dot = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x**2 for x in a))
    nb = math.sqrt(sum(x**2 for x in b))
    return dot/(na*nb) if na and nb else 0

print(f"\n  Similarity (TF-IDF):")
for i in range(len(docs)):
    for j in range(i+1, len(docs)):
        sim = cosine_sim(tfidf[i], tfidf[j])
        print(f"    Doc{i} vs Doc{j}: {sim:.3f}")

print("\nDone!")
