"""
Recurrent Neural Networks
=========================
Section 03

Demonstrates RNN concepts: simple RNN cell,
sequence processing, and character prediction.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("1. SIMPLE RNN CELL")
print("=" * 60)

def sigmoid(x): return 1 / (1 + math.exp(-max(-500, min(500, x))))

class RNNCell:
    def __init__(self, input_size, hidden_size):
        random.seed(42)
        self.Wx = [[random.gauss(0, 0.5) for _ in range(input_size)] for _ in range(hidden_size)]
        self.Wh = [[random.gauss(0, 0.5) for _ in range(hidden_size)] for _ in range(hidden_size)]
        self.b = [0.0] * hidden_size
        self.hidden_size = hidden_size

    def forward(self, x, h_prev):
        h_new = []
        for i in range(self.hidden_size):
            val = self.b[i]
            val += sum(self.Wx[i][j] * x[j] for j in range(len(x)))
            val += sum(self.Wh[i][j] * h_prev[j] for j in range(self.hidden_size))
            h_new.append(math.tanh(val))
        return h_new

rnn = RNNCell(input_size=3, hidden_size=4)
h = [0.0] * 4
sequence = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0]]

print("  Processing sequence:")
for t, x in enumerate(sequence):
    h = rnn.forward(x, h)
    print(f"    t={t}: input={x} -> hidden=[{', '.join(f'{v:.3f}' for v in h)}]")

print("\n" + "=" * 60)
print("2. CHARACTER-LEVEL PREDICTION")
print("=" * 60)

text = "hello world hello"
chars = sorted(set(text))
char_to_idx = {c: i for i, c in enumerate(chars)}
print(f"  Vocabulary: {chars}")
print(f"  Bigram frequencies:")

from collections import Counter
bigrams = Counter(text[i:i+2] for i in range(len(text)-1))
for bg, count in bigrams.most_common(5):
    print(f"    '{bg}': {count}")

print("\nDone!")
