"""
Fine-Tuning LLMs
================
Section 07

Demonstrates fine-tuning concepts: training loops,
LoRA simulation, and evaluation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("FINE-TUNING LLMs")
print("=" * 60)

# 1. Training Loop Simulation
print("\n1. TRAINING LOOP")
print("-" * 40)

random.seed(42)

class FineTuner:
    def __init__(self, base_loss=2.5):
        self.loss = base_loss
        self.history = []
    def train_step(self, lr=0.001):
        improvement = lr * random.gauss(10, 3)
        self.loss = max(0.1, self.loss - improvement)
        self.history.append(self.loss)
        return self.loss

tuner = FineTuner(2.5)
for epoch in range(10):
    loss = tuner.train_step(0.001)
    bar = "#" * int((2.5 - loss) * 15)
    print(f"  Epoch {epoch+1:2d}: loss={loss:.4f} {bar}")

# 2. LoRA (Low-Rank Adaptation)
print("\n2. LoRA PARAMETER EFFICIENCY")
print("-" * 40)

def lora_savings(d, r):
    full_params = d * d
    lora_params = 2 * d * r
    savings = (1 - lora_params / full_params) * 100
    return full_params, lora_params, savings

print(f"  {'Dim':>6} {'Rank':>5} {'Full':>10} {'LoRA':>10} {'Savings':>8}")
for d in [768, 1024, 4096]:
    for r in [4, 8, 16]:
        full, lora, savings = lora_savings(d, r)
        print(f"  {d:>6} {r:>5} {full:>10,} {lora:>10,} {savings:>7.1f}%")

# 3. Evaluation
print("\n3. MODEL EVALUATION")
print("-" * 40)

metrics = {
    "Base Model": {"accuracy": 0.72, "f1": 0.68, "perplexity": 45.2},
    "Fine-tuned (1 epoch)": {"accuracy": 0.81, "f1": 0.78, "perplexity": 28.1},
    "Fine-tuned (5 epochs)": {"accuracy": 0.89, "f1": 0.87, "perplexity": 15.3},
    "Fine-tuned (10 epochs)": {"accuracy": 0.91, "f1": 0.90, "perplexity": 12.1},
}

print(f"  {'Model':25s} {'Acc':>6} {'F1':>6} {'PPL':>8}")
for name, m in metrics.items():
    print(f"  {name:25s} {m['accuracy']:>6.2f} {m['f1']:>6.2f} {m['perplexity']:>8.1f}")

print("\nDone!")
