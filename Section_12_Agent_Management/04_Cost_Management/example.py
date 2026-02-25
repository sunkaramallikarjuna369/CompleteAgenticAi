"""
Cost Management
===============
Section 12

Demonstrates cost management: token budgets,
cost tracking, and optimization.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("AGENT COST MANAGEMENT")
print("=" * 60)

# 1. Token Budget
print("\n1. TOKEN BUDGET TRACKER")
print("-" * 40)

class TokenBudget:
    def __init__(self, daily_limit=100000):
        self.daily_limit = daily_limit
        self.used = 0
        self.requests = []
    def use(self, tokens, model="gpt-4"):
        cost_per_token = {"gpt-4": 0.00003, "gpt-3.5": 0.000001}
        cost = tokens * cost_per_token.get(model, 0.00001)
        self.used += tokens
        self.requests.append({"tokens": tokens, "model": model, "cost": cost})
        remaining = self.daily_limit - self.used
        status = "OK" if remaining > 0 else "EXCEEDED"
        print(f"  Used {tokens:>6} tokens ({model:8s}) | Total: {self.used:>7}/{self.daily_limit} [{status}] ${cost:.4f}")
        return remaining > 0

budget = TokenBudget(50000)
random.seed(42)
for _ in range(6):
    tokens = random.randint(5000, 15000)
    model = random.choice(["gpt-4", "gpt-3.5"])
    budget.use(tokens, model)

total_cost = sum(r["cost"] for r in budget.requests)
print(f"\n  Total cost: ${total_cost:.4f}")
print(f"  Budget usage: {budget.used/budget.daily_limit:.0%}")

# 2. Cost Optimization
print("\n2. COST OPTIMIZATION STRATEGIES")
print("-" * 40)

strategies = [
    ("Caching", "Cache frequent queries", 0.40),
    ("Model routing", "Use cheaper model when possible", 0.30),
    ("Prompt compression", "Reduce input token count", 0.15),
    ("Batch requests", "Group similar requests", 0.10),
]

print(f"  {'Strategy':22s} {'Savings':>8}")
for name, desc, savings in strategies:
    bar = "#" * int(savings * 30)
    print(f"  {name:22s} {bar} {savings:.0%}")

print(f"\n  Combined potential savings: {sum(s for _,_,s in strategies):.0%}")

print("\nDone!")
