"""
Neural Network Fundamentals
===========================
Section 03

Demonstrates NN basics: activation functions,
forward propagation, and backpropagation (XOR).

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("1. ACTIVATION FUNCTIONS")
print("=" * 60)

def sigmoid(x): return 1 / (1 + math.exp(-max(-500, min(500, x))))
def relu(x): return max(0, x)
def tanh_fn(x): return math.tanh(x)

for name, fn in [("Sigmoid", sigmoid), ("ReLU", relu), ("Tanh", tanh_fn)]:
    vals = [fn(x) for x in [-2, -1, 0, 1, 2]]
    print(f"  {name:8s}: {[f'{v:.3f}' for v in vals]}")

print("\n" + "=" * 60)
print("2. NEURAL NETWORK SOLVING XOR")
print("=" * 60)

random.seed(42)
# 2-layer NN: 2 inputs -> 2 hidden -> 1 output
w1 = [[random.gauss(0, 1) for _ in range(2)] for _ in range(2)]
b1 = [random.gauss(0, 0.5) for _ in range(2)]
w2 = [random.gauss(0, 1) for _ in range(2)]
b2 = random.gauss(0, 0.5)

def forward(x):
    h = [sigmoid(sum(w1[i][j]*x[j] for j in range(2)) + b1[i]) for i in range(2)]
    o = sigmoid(sum(w2[i]*h[i] for i in range(2)) + b2)
    return h, o

XOR = [([0,0], 0), ([0,1], 1), ([1,0], 1), ([1,1], 0)]
lr = 2.0

for epoch in range(3000):
    for x, target in XOR:
        h, o = forward(x)
        do = o * (1 - o) * (target - o)
        dh = [h[i] * (1 - h[i]) * do * w2[i] for i in range(2)]
        for i in range(2):
            w2[i] += lr * do * h[i]
        b2 += lr * do
        for i in range(2):
            for j in range(2):
                w1[i][j] += lr * dh[i] * x[j]
            b1[i] += lr * dh[i]

print("  XOR Results after training:")
for x, target in XOR:
    _, o = forward(x)
    print(f"    {x} -> {o:.4f} (target: {target})")

print("\nDone!")
