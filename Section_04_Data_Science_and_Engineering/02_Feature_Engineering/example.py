"""
Feature Engineering
===================
Section 04

Demonstrates feature engineering: scaling, encoding,
polynomial features, and correlation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("1. FEATURE SCALING")
print("=" * 60)

random.seed(42)
data = [random.gauss(50, 15) for _ in range(20)]

mn, mx = min(data), max(data)
normalized = [(x - mn) / (mx - mn) for x in data]
mean = sum(data) / len(data)
std = math.sqrt(sum((x - mean)**2 for x in data) / len(data))
standardized = [(x - mean) / std for x in data]

print(f"  Original:     min={mn:.1f}, max={mx:.1f}, mean={mean:.1f}")
print(f"  Normalized:   min={min(normalized):.1f}, max={max(normalized):.1f}")
print(f"  Standardized: mean={sum(standardized)/len(standardized):.2f}, std={math.sqrt(sum(x**2 for x in standardized)/len(standardized)):.2f}")

print("\n" + "=" * 60)
print("2. CATEGORICAL ENCODING")
print("=" * 60)

categories = ["red", "green", "blue", "red", "blue"]
unique = sorted(set(categories))
print(f"  Categories: {categories}")

# One-hot
print("  One-hot encoding:")
for val in categories[:3]:
    encoded = [1 if u == val else 0 for u in unique]
    print(f"    {val:6s} -> {encoded}")

# Label encoding
label_map = {c: i for i, c in enumerate(unique)}
print(f"  Label encoding: {label_map}")

print("\n" + "=" * 60)
print("3. POLYNOMIAL FEATURES")
print("=" * 60)

X = [[1, 2], [3, 4], [5, 6]]
print("  Original -> Polynomial (degree=2):")
for x in X:
    poly = [x[0], x[1], x[0]**2, x[0]*x[1], x[1]**2]
    print(f"    {x} -> {poly}")

print("\nDone!")
