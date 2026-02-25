"""
AI Ethics
=========
Section 14

Demonstrates AI ethics: fairness metrics,
transparency, and ethical evaluation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("AI ETHICS")
print("=" * 60)

class EthicsEvaluator:
    def __init__(self):
        self.principles = {
            "fairness": "Equal treatment regardless of attributes",
            "transparency": "Explainable decisions",
            "accountability": "Clear responsibility for AI actions",
            "privacy": "Protection of personal data",
            "beneficence": "AI should benefit humanity",
        }
    def evaluate(self, scores):
        results = {}
        for p, desc in self.principles.items():
            s = scores.get(p, 0)
            status = "PASS" if s >= 0.8 else "WARN" if s >= 0.5 else "FAIL"
            results[p] = {"score": s, "status": status}
        return results

evaluator = EthicsEvaluator()
scores = {"fairness": 0.72, "transparency": 0.85, "accountability": 0.90,
          "privacy": 0.65, "beneficence": 0.88}

results = evaluator.evaluate(scores)
print("  Ethics Evaluation:")
for p, data in results.items():
    indicator = {"PASS": "[OK]", "WARN": "[!!]", "FAIL": "[XX]"}[data["status"]]
    bar = "#" * int(data["score"] * 20)
    print(f"  {p:18s} {bar:20s} {data['score']:.2f} {indicator}")

# Fairness check
print("\n  DEMOGRAPHIC PARITY CHECK")
random.seed(42)
groups = {"A": 0.65, "B": 0.63, "C": 0.45}
for g, rate in groups.items():
    bar = "#" * int(rate * 40)
    print(f"  Group {g}: {bar} {rate:.0%}")
disparity = max(groups.values()) - min(groups.values())
print(f"  Disparity: {disparity:.0%} ({'FAIR' if disparity < 0.1 else 'UNFAIR'})")

print("\nDone!")
