"""
Human Oversight
===============
Section 12

Demonstrates human oversight: approval gates,
escalation policies, and feedback loops.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("HUMAN OVERSIGHT")
print("=" * 60)

# 1. Approval Gates
print("\n1. APPROVAL GATE SYSTEM")
print("-" * 40)

class ApprovalGate:
    def __init__(self):
        self.gates = []
    def add_gate(self, name, condition, auto_approve=False):
        self.gates.append({"name": name, "condition": condition, "auto": auto_approve})
    def check(self, action):
        for gate in self.gates:
            if gate["condition"](action):
                if gate["auto"]:
                    print(f"  [AUTO-APPROVED] {gate['name']}: {action['type']}")
                else:
                    print(f"  [NEEDS APPROVAL] {gate['name']}: {action['type']}")
                    return False
        print(f"  [APPROVED] No gates triggered: {action['type']}")
        return True

gates = ApprovalGate()
gates.add_gate("High cost", lambda a: a.get("cost", 0) > 10, auto_approve=False)
gates.add_gate("External API", lambda a: a.get("external", False), auto_approve=False)
gates.add_gate("Low risk", lambda a: a.get("risk", "") == "low", auto_approve=True)

actions = [
    {"type": "search_docs", "cost": 0.01, "risk": "low"},
    {"type": "call_external_api", "cost": 5, "external": True},
    {"type": "deploy_model", "cost": 50, "risk": "high"},
]

for action in actions:
    gates.check(action)
    print()

# 2. Escalation Policy
print("2. ESCALATION POLICY")
print("-" * 40)

class EscalationPolicy:
    def __init__(self):
        self.levels = []
    def add_level(self, name, condition):
        self.levels.append({"name": name, "condition": condition})
    def evaluate(self, situation):
        for level in self.levels:
            if level["condition"](situation):
                return level["name"]
        return "No escalation needed"

policy = EscalationPolicy()
policy.add_level("L1: Notify human", lambda s: s.get("confidence", 1) < 0.5)
policy.add_level("L2: Pause and wait", lambda s: s.get("errors", 0) > 3)
policy.add_level("L3: Full stop", lambda s: s.get("safety_violation", False))

situations = [
    {"confidence": 0.3, "errors": 0},
    {"confidence": 0.8, "errors": 5},
    {"confidence": 0.9, "safety_violation": True},
    {"confidence": 0.9, "errors": 0},
]

for sit in situations:
    result = policy.evaluate(sit)
    print(f"  {sit} -> {result}")

print("\nDone!")
