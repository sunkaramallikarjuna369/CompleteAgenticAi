"""
Self-Reflection
===============
Section 08

Demonstrates agent self-reflection: output evaluation,
error analysis, and strategy adjustment.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("AGENT SELF-REFLECTION")
print("=" * 60)

class ReflectiveAgent:
    def __init__(self):
        self.attempts = []
        self.strategy = "default"

    def evaluate_output(self, output, criteria):
        scores = {}
        for criterion, check_fn in criteria.items():
            scores[criterion] = check_fn(output)
        overall = sum(scores.values()) / len(scores)
        return scores, overall

    def reflect(self, scores, threshold=0.7):
        failed = [k for k, v in scores.items() if v < threshold]
        if not failed:
            return "Output meets all criteria"
        return f"Need to improve: {', '.join(failed)}"

    def adjust_strategy(self, reflection):
        if "improve" in reflection:
            self.strategy = "detailed"
            return "Switching to detailed strategy"
        return "Keeping current strategy"

agent = ReflectiveAgent()

# Simulate reflection loop
print("\n  Self-Reflection Loop:")
criteria = {
    "completeness": lambda o: 0.8 if len(o) > 50 else 0.3,
    "accuracy": lambda o: random.random() * 0.5 + 0.5,
    "clarity": lambda o: 0.9 if "step" in o.lower() else 0.4,
}

random.seed(42)
outputs = [
    "AI agents are useful",
    "Step 1: AI agents perceive. Step 2: They reason. Step 3: They act autonomously to complete complex tasks.",
]

for i, output in enumerate(outputs):
    print(f"\n  Attempt {i+1}: '{output[:60]}...'")
    scores, overall = agent.evaluate_output(output, criteria)
    for criterion, score in scores.items():
        bar = "#" * int(score * 10)
        print(f"    {criterion:15s}: {bar:10s} ({score:.2f})")
    print(f"    Overall: {overall:.2f}")
    reflection = agent.reflect(scores)
    print(f"    Reflection: {reflection}")
    adjustment = agent.adjust_strategy(reflection)
    print(f"    Strategy: {adjustment}")

print("\nDone!")
