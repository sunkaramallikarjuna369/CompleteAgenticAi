"""
Cloud Architecture for AI
=========================
Section 15

Demonstrates cloud architecture: service models,
scaling, and cost estimation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("CLOUD ARCHITECTURE FOR AI")
print("=" * 60)

# Service Models
print("\n1. CLOUD SERVICE MODELS")
print("-" * 40)

models = {
    "IaaS": {"manage": "OS, Runtime, App", "examples": "EC2, GCE, Azure VMs"},
    "PaaS": {"manage": "App, Data", "examples": "Heroku, App Engine"},
    "SaaS": {"manage": "Config only", "examples": "OpenAI API, Gmail"},
}
for m, info in models.items():
    print(f"  {m}: You manage: {info['manage']}")
    print(f"       Examples: {info['examples']}\n")

# Auto-Scaling
print("2. AUTO-SCALING SIMULATION")
print("-" * 40)

class AutoScaler:
    def __init__(self, min_inst=1, max_inst=5, target_cpu=70):
        self.min = min_inst
        self.max = max_inst
        self.target = target_cpu
        self.current = min_inst
    def scale(self, cpu):
        if cpu > self.target + 10:
            self.current = min(self.current + 1, self.max)
            return "SCALE UP"
        elif cpu < self.target - 20 and self.current > self.min:
            self.current = max(self.current - 1, self.min)
            return "SCALE DOWN"
        return "STEADY"

scaler = AutoScaler()
for cpu in [30, 55, 82, 90, 75, 50, 30]:
    action = scaler.scale(cpu)
    print(f"  CPU={cpu:>3}% | Instances={scaler.current} | {action}")

# Cost Estimation
print("\n3. MONTHLY COST ESTIMATE")
print("-" * 40)

costs = {"Compute (720h)": 72.0, "Storage (100GB)": 2.30, "API calls (5M)": 5.0, "GPU (100h)": 306.0}
total = sum(costs.values())
for item, cost in costs.items():
    print(f"  {item:25s}: ${cost:>8.2f}")
print(f"  {'TOTAL':25s}: ${total:>8.2f}")

print("\nDone!")
