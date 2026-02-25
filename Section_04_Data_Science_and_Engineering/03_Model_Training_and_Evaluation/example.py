"""
Model Training and Evaluation
=============================
Section 04

Demonstrates training: grid search, cross-validation,
and learning curves.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("1. GRID SEARCH HYPERPARAMETER TUNING")
print("=" * 60)

random.seed(42)

def simulate_accuracy(lr, n_trees, depth):
    base = 0.7
    base += 0.1 * (1 - abs(lr - 0.1) * 5)
    base += 0.05 * min(n_trees / 100, 1)
    base += 0.03 * min(depth / 10, 1)
    return min(0.99, base + random.gauss(0, 0.02))

param_grid = {
    "lr": [0.01, 0.05, 0.1, 0.2],
    "n_trees": [50, 100, 200],
    "depth": [5, 10, 15],
}

best_score, best_params = 0, {}
print(f"  Grid search ({len(param_grid['lr'])*len(param_grid['n_trees'])*len(param_grid['depth'])} combinations):")
for lr in param_grid["lr"]:
    for nt in param_grid["n_trees"]:
        for d in param_grid["depth"]:
            score = simulate_accuracy(lr, nt, d)
            if score > best_score:
                best_score = score
                best_params = {"lr": lr, "n_trees": nt, "depth": d}

print(f"  Best: {best_params} -> {best_score:.4f}")

print("\n" + "=" * 60)
print("2. K-FOLD CROSS VALIDATION")
print("=" * 60)

data = list(range(100))
random.shuffle(data)
k = 5
fold_size = len(data) // k
scores = []
for i in range(k):
    test = data[i*fold_size:(i+1)*fold_size]
    train = data[:i*fold_size] + data[(i+1)*fold_size:]
    score = 0.85 + random.gauss(0, 0.03)
    scores.append(score)
    print(f"  Fold {i+1}: train={len(train)}, test={len(test)}, score={score:.3f}")

print(f"  Mean: {sum(scores)/len(scores):.3f} +/- {math.sqrt(sum((s-sum(scores)/len(scores))**2 for s in scores)/len(scores)):.3f}")

print("\nDone!")
