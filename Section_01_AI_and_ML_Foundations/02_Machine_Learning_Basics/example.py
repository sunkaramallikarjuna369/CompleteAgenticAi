"""
Machine Learning Basics
=======================
Section 01

Demonstrates ML fundamentals: linear regression,
evaluation metrics, and train-test split.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("1. LINEAR REGRESSION FROM SCRATCH")
print("=" * 60)

random.seed(42)
X = [i for i in range(20)]
Y = [2 * x + 3 + random.gauss(0, 2) for x in X]

n = len(X)
x_mean = sum(X) / n
y_mean = sum(Y) / n
num = sum((X[i] - x_mean) * (Y[i] - y_mean) for i in range(n))
den = sum((X[i] - x_mean) ** 2 for i in range(n))
slope = num / den
intercept = y_mean - slope * x_mean

print(f"  y = {slope:.2f}x + {intercept:.2f}  (true: y = 2x + 3)")

predictions = [slope * x + intercept for x in X]
mse = sum((Y[i] - predictions[i]) ** 2 for i in range(n)) / n
r2 = 1 - sum((Y[i] - predictions[i]) ** 2 for i in range(n)) / sum((Y[i] - y_mean) ** 2 for i in range(n))
print(f"  MSE: {mse:.4f}, R²: {r2:.4f}")

print("\n" + "=" * 60)
print("2. TRAIN-TEST SPLIT")
print("=" * 60)

data = list(range(100))
random.shuffle(data)
split = int(0.8 * len(data))
train, test = data[:split], data[split:]
print(f"  Total: {len(data)}, Train: {len(train)}, Test: {len(test)}")

print("\n" + "=" * 60)
print("3. EVALUATION METRICS")
print("=" * 60)

actual =    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
predicted = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

tp = sum(a == 1 and p == 1 for a, p in zip(actual, predicted))
fp = sum(a == 0 and p == 1 for a, p in zip(actual, predicted))
fn = sum(a == 1 and p == 0 for a, p in zip(actual, predicted))
precision = tp / (tp + fp) if (tp + fp) else 0
recall = tp / (tp + fn) if (tp + fn) else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

print(f"  Precision: {precision:.2f}")
print(f"  Recall:    {recall:.2f}")
print(f"  F1 Score:  {f1:.2f}")

print("\nDone!")
