"""
Responsible AI
==============
Section 14

Demonstrates responsible AI: model cards,
impact assessments, and audit trails.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

from datetime import datetime

print("=" * 60)
print("RESPONSIBLE AI")
print("=" * 60)

# 1. Model Card
print("\n1. MODEL CARD")
print("-" * 40)

card = {
    "model": "SentimentClassifier v1.0",
    "use": "Classify customer feedback",
    "limitations": ["English only", "Not for medical/legal advice"],
    "ethics": ["Tested for demographic bias", "Regular fairness audits"],
    "metrics": {"accuracy": 0.92, "f1": 0.89, "fairness_gap": 0.04},
}

print(f"  Model: {card['model']}")
print(f"  Use: {card['use']}")
print(f"  Limitations: {', '.join(card['limitations'])}")
print(f"  Ethics: {', '.join(card['ethics'])}")
print(f"  Metrics: {card['metrics']}")

# 2. Audit Trail
print("\n2. AUDIT TRAIL")
print("-" * 40)

class AuditTrail:
    def __init__(self):
        self.entries = []
    def log(self, action, actor, details=""):
        self.entries.append({"action": action, "actor": actor, "details": details})
    def show(self):
        for e in self.entries:
            print(f"  [{e['actor']:12s}] {e['action']:25s} {e['details'][:30]}")

audit = AuditTrail()
audit.log("model_deployed", "system", "v1.0 to production")
audit.log("prediction_made", "api", "batch of 100 requests")
audit.log("fairness_check", "auditor", "demographic parity: 0.04")
audit.log("model_updated", "engineer", "retrained with new data")
audit.show()

print("\nDone!")
