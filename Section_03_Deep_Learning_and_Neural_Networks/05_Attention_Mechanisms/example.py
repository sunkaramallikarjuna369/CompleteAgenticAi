"""
Attention Mechanisms
====================
Section 03

Demonstrates attention: additive attention,
multi-head attention, and visualization.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("1. ADDITIVE (BAHDANAU) ATTENTION")
print("=" * 60)

random.seed(42)

def softmax(x):
    m = max(x)
    exps = [math.exp(v - m) for v in x]
    s = sum(exps)
    return [e / s for e in exps]

class AdditiveAttention:
    def __init__(self, dim):
        self.W1 = [random.gauss(0, 0.5) for _ in range(dim)]
        self.W2 = [random.gauss(0, 0.5) for _ in range(dim)]
        self.v = [random.gauss(0, 0.5) for _ in range(dim)]

    def score(self, query, key):
        combined = [math.tanh(self.W1[i]*query[i] + self.W2[i]*key[i]) for i in range(len(query))]
        return sum(self.v[i]*combined[i] for i in range(len(combined)))

    def attend(self, query, keys, values):
        scores = [self.score(query, k) for k in keys]
        weights = softmax(scores)
        output = [0.0] * len(values[0])
        for j, w in enumerate(weights):
            for k in range(len(output)):
                output[k] += w * values[j][k]
        return output, weights

dim = 4
attn = AdditiveAttention(dim)
query = [random.gauss(0, 1) for _ in range(dim)]
keys = [[random.gauss(0, 1) for _ in range(dim)] for _ in range(5)]
values = [[random.gauss(0, 1) for _ in range(dim)] for _ in range(5)]

out, wts = attn.attend(query, keys, values)
print("  Attention weights:")
for i, w in enumerate(wts):
    bar = "#" * int(w * 30)
    print(f"    Key {i}: {bar} ({w:.3f})")

print("\n" + "=" * 60)
print("2. MULTI-HEAD ATTENTION")
print("=" * 60)

def multi_head_attention(Q, K, V, n_heads=2):
    d = len(Q[0])
    head_dim = d // n_heads
    all_outputs = []
    for h in range(n_heads):
        start = h * head_dim
        end = start + head_dim
        Qh = [q[start:end] for q in Q]
        Kh = [k[start:end] for k in K]
        Vh = [v[start:end] for v in V]

        scores = []
        for i in range(len(Qh)):
            row = [sum(Qh[i][d]*Kh[j][d] for d in range(head_dim)) / math.sqrt(head_dim) for j in range(len(Kh))]
            scores.append(softmax(row))

        head_out = []
        for i in range(len(Qh)):
            out = [sum(scores[i][j]*Vh[j][d] for j in range(len(Vh))) for d in range(head_dim)]
            head_out.append(out)
        all_outputs.append(head_out)

    concatenated = []
    for i in range(len(Q)):
        row = []
        for h in range(n_heads):
            row.extend(all_outputs[h][i])
        concatenated.append(row)
    return concatenated

seq = [[random.gauss(0, 1) for _ in range(4)] for _ in range(3)]
result = multi_head_attention(seq, seq, seq, n_heads=2)
print(f"  Input: {len(seq)} tokens x {len(seq[0])} dims")
print(f"  Output: {len(result)} tokens x {len(result[0])} dims")

print("\nDone!")
