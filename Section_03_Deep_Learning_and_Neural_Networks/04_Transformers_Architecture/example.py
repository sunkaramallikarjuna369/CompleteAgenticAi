"""
Transformers Architecture
=========================
Section 03

Demonstrates Transformer concepts: self-attention,
positional encoding, and a transformer block.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("1. SELF-ATTENTION MECHANISM")
print("=" * 60)

def softmax(x):
    m = max(x)
    exps = [math.exp(v - m) for v in x]
    s = sum(exps)
    return [e / s for e in exps]

def self_attention(Q, K, V):
    d_k = len(Q[0])
    scores = []
    for i in range(len(Q)):
        row = []
        for j in range(len(K)):
            dot = sum(Q[i][k] * K[j][k] for k in range(d_k))
            row.append(dot / math.sqrt(d_k))
        scores.append(softmax(row))

    output = []
    for i in range(len(Q)):
        out = [0.0] * len(V[0])
        for j in range(len(V)):
            for k in range(len(V[0])):
                out[k] += scores[i][j] * V[j][k]
        output.append(out)
    return output, scores

random.seed(42)
seq_len, d_model = 4, 3
Q = [[random.gauss(0, 1) for _ in range(d_model)] for _ in range(seq_len)]
K = [[random.gauss(0, 1) for _ in range(d_model)] for _ in range(seq_len)]
V = [[random.gauss(0, 1) for _ in range(d_model)] for _ in range(seq_len)]

output, weights = self_attention(Q, K, V)
print("  Attention weights:")
for i, row in enumerate(weights):
    print(f"    Token {i}: [{', '.join(f'{w:.3f}' for w in row)}]")

print("\n" + "=" * 60)
print("2. POSITIONAL ENCODING")
print("=" * 60)

def positional_encoding(seq_len, d_model):
    pe = []
    for pos in range(seq_len):
        row = []
        for i in range(d_model):
            if i % 2 == 0:
                row.append(math.sin(pos / (10000 ** (i / d_model))))
            else:
                row.append(math.cos(pos / (10000 ** ((i-1) / d_model))))
        pe.append(row)
    return pe

pe = positional_encoding(4, 6)
print("  Positional Encodings (4 positions, 6 dims):")
for pos, enc in enumerate(pe):
    print(f"    Pos {pos}: [{', '.join(f'{v:+.3f}' for v in enc)}]")

print("\nDone!")
