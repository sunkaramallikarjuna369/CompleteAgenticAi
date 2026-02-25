"""
Supervised Learning
===================
Section 01

Demonstrates supervised learning: k-NN, Decision Tree,
and Naive Bayes classifiers.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random
from collections import Counter

print("=" * 60)
print("1. K-NEAREST NEIGHBORS")
print("=" * 60)

def knn(train, query, k=3):
    dists = []
    for point, label in train:
        d = math.sqrt(sum((a - b) ** 2 for a, b in zip(point, query)))
        dists.append((d, label))
    dists.sort()
    top_k = [label for _, label in dists[:k]]
    return Counter(top_k).most_common(1)[0][0]

train = [([1, 2], "A"), ([2, 3], "A"), ([3, 1], "A"),
         ([6, 5], "B"), ([7, 8], "B"), ([8, 6], "B")]

for query in ([2, 2], [7, 7], [4, 4]):
    result = knn(train, query)
    print(f"  {query} -> {result}")

print("\n" + "=" * 60)
print("2. SIMPLE DECISION TREE")
print("=" * 60)

class DecisionNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label

    def predict(self, x):
        if self.label is not None:
            return self.label
        if x[self.feature] <= self.threshold:
            return self.left.predict(x)
        return self.right.predict(x)

tree = DecisionNode(feature=0, threshold=5,
    left=DecisionNode(label="Cat"),
    right=DecisionNode(feature=1, threshold=3,
        left=DecisionNode(label="Dog"),
        right=DecisionNode(label="Horse")))

for x in ([3, 2], [7, 2], [8, 5]):
    print(f"  {x} -> {tree.predict(x)}")

print("\n" + "=" * 60)
print("3. NAIVE BAYES")
print("=" * 60)

def naive_bayes(data, query):
    classes = set(d[-1] for d in data)
    best_class, best_prob = None, -1
    for cls in classes:
        cls_data = [d for d in data if d[-1] == cls]
        prob = len(cls_data) / len(data)
        for i, val in enumerate(query):
            matches = sum(1 for d in cls_data if d[i] == val)
            prob *= (matches + 1) / (len(cls_data) + 2)
        if prob > best_prob:
            best_class, best_prob = cls, prob
    return best_class

data = [["sunny", "hot", "No"], ["sunny", "mild", "No"],
        ["cloudy", "hot", "Yes"], ["rainy", "mild", "Yes"],
        ["cloudy", "mild", "Yes"], ["rainy", "hot", "No"]]

print(f"  ['sunny', 'mild'] -> {naive_bayes(data, ['sunny', 'mild'])}")
print(f"  ['cloudy', 'hot'] -> {naive_bayes(data, ['cloudy', 'hot'])}")

print("\nDone!")
