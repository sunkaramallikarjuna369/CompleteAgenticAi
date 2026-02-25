"""
Transfer Learning
=================
Section 02

Demonstrates transfer learning concepts: feature extraction,
fine-tuning simulation, and domain adaptation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("1. PRETRAINED FEATURE EXTRACTOR")
print("=" * 60)

class PretrainedModel:
    def __init__(self, n_features=5):
        random.seed(42)
        self.weights = [[random.gauss(0, 1) for _ in range(10)] for _ in range(n_features)]
    def extract_features(self, input_data):
        return [sum(w * x for w, x in zip(self.weights[i], input_data)) for i in range(len(self.weights))]

model = PretrainedModel(5)
sample = [random.gauss(0, 1) for _ in range(10)]
features = model.extract_features(sample)
print(f"  Input (10 dims): [{', '.join(f'{v:.2f}' for v in sample[:5])}...]")
print(f"  Features (5 dims): [{', '.join(f'{v:.2f}' for v in features)}]")

print("\n" + "=" * 60)
print("2. FINE-TUNING SIMULATION")
print("=" * 60)

class FineTuner:
    def __init__(self, base_accuracy=0.65):
        self.base = base_accuracy
        self.current = base_accuracy
    def train_epoch(self, lr=0.05):
        improvement = lr * random.gauss(0.1, 0.05)
        self.current = min(0.99, self.current + improvement)
        return self.current

random.seed(42)
tuner = FineTuner(0.65)
print(f"  Base accuracy: {tuner.base:.0%}")
for ep in range(8):
    acc = tuner.train_epoch()
    bar = "#" * int(acc * 30)
    print(f"  Epoch {ep+1}: {bar} {acc:.1%}")

print("\n" + "=" * 60)
print("3. TRANSFER vs FROM SCRATCH")
print("=" * 60)

data = [
    ("Epochs", "Transfer", "Scratch"),
    ("1", "72%", "45%"),
    ("5", "88%", "62%"),
    ("10", "93%", "75%"),
    ("20", "95%", "85%"),
]
for row in data:
    print(f"  {row[0]:>8} {row[1]:>10} {row[2]:>10}")

print("\nDone!")
