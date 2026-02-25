"""
Classical ML Algorithms
=======================
Section 01

Demonstrates classical algorithms: Logistic Regression,
Random Forest, and cross-validation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("1. LOGISTIC REGRESSION")
print("=" * 60)

random.seed(42)

def sigmoid(z):
    return 1 / (1 + math.exp(-max(-500, min(500, z))))

X = [[random.gauss(0, 1), random.gauss(0, 1)] for _ in range(100)]
y = [1 if x[0] + x[1] + random.gauss(0, 0.3) > 0 else 0 for x in X]

w = [0.0, 0.0]
b = 0.0
lr = 0.1

for epoch in range(100):
    for i in range(len(X)):
        z = sum(w[j] * X[i][j] for j in range(2)) + b
        pred = sigmoid(z)
        error = pred - y[i]
        for j in range(2):
            w[j] -= lr * error * X[i][j]
        b -= lr * error

correct = sum(1 for i in range(len(X))
    if (sigmoid(sum(w[j]*X[i][j] for j in range(2))+b) >= 0.5) == (y[i] == 1))
print(f"  Weights: [{w[0]:.3f}, {w[1]:.3f}], Bias: {b:.3f}")
print(f"  Accuracy: {correct}/{len(X)} ({correct/len(X):.0%})")

print("\n" + "=" * 60)
print("2. RANDOM FOREST (simplified)")
print("=" * 60)

class SimpleTree:
    def __init__(self, feature, threshold, left_label, right_label):
        self.feature = feature
        self.threshold = threshold
        self.left_label = left_label
        self.right_label = right_label
    def predict(self, x):
        return self.left_label if x[self.feature] <= self.threshold else self.right_label

class RandomForest:
    def __init__(self, n_trees=5):
        self.trees = []
        self.n_trees = n_trees
    def fit(self, X, y):
        for _ in range(self.n_trees):
            idx = [random.randint(0, len(X)-1) for _ in range(len(X))]
            feat = random.randint(0, len(X[0])-1)
            vals = [X[i][feat] for i in idx]
            thresh = sum(vals) / len(vals)
            left_labels = [y[i] for i in idx if X[i][feat] <= thresh]
            right_labels = [y[i] for i in idx if X[i][feat] > thresh]
            ll = max(set(left_labels), key=left_labels.count) if left_labels else 0
            rl = max(set(right_labels), key=right_labels.count) if right_labels else 1
            self.trees.append(SimpleTree(feat, thresh, ll, rl))
    def predict(self, x):
        votes = [t.predict(x) for t in self.trees]
        return max(set(votes), key=votes.count)

rf = RandomForest(n_trees=11)
rf.fit(X, y)
correct = sum(1 for i in range(len(X)) if rf.predict(X[i]) == y[i])
print(f"  Trees: {rf.n_trees}, Accuracy: {correct/len(X):.0%}")

print("\n" + "=" * 60)
print("3. K-FOLD CROSS VALIDATION")
print("=" * 60)

def k_fold_cv(X, y, k=5):
    n = len(X)
    fold_size = n // k
    scores = []
    for i in range(k):
        test_idx = set(range(i*fold_size, min((i+1)*fold_size, n)))
        train_X = [X[j] for j in range(n) if j not in test_idx]
        train_y = [y[j] for j in range(n) if j not in test_idx]
        test_X = [X[j] for j in test_idx]
        test_y = [y[j] for j in test_idx]
        rf2 = RandomForest(7)
        rf2.fit(train_X, train_y)
        acc = sum(1 for j in range(len(test_X)) if rf2.predict(test_X[j]) == test_y[j]) / len(test_X)
        scores.append(acc)
    return scores

scores = k_fold_cv(X, y, k=5)
print(f"  Fold accuracies: {[f'{s:.2f}' for s in scores]}")
print(f"  Mean: {sum(scores)/len(scores):.2f}")

print("\nDone!")
