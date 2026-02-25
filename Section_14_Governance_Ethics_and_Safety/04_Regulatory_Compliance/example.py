"""
Regulatory Compliance
=====================
Section 14

Demonstrates compliance: GDPR checks, data policies,
and compliance reporting.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("REGULATORY COMPLIANCE")
print("=" * 60)

class ComplianceChecker:
    def __init__(self):
        self.rules = []
    def add_rule(self, name, category, check_fn, desc):
        self.rules.append({"name": name, "cat": category, "check": check_fn, "desc": desc})
    def audit(self, system):
        results = {"pass": [], "fail": []}
        for rule in self.rules:
            if rule["check"](system):
                results["pass"].append(rule)
            else:
                results["fail"].append(rule)
        return results

checker = ComplianceChecker()
checker.add_rule("Consent", "GDPR", lambda s: s.get("consent", False), "User consent required")
checker.add_rule("Deletion", "GDPR", lambda s: s.get("deletion", False), "Right to deletion")
checker.add_rule("Encryption", "Security", lambda s: s.get("encrypted", False), "Data encryption")
checker.add_rule("Bias testing", "Ethics", lambda s: s.get("bias_tested", False), "Model bias testing")
checker.add_rule("Explainability", "Ethics", lambda s: s.get("explainable", False), "Decision explainability")

system = {"consent": True, "deletion": True, "encrypted": True, "bias_tested": False, "explainable": False}

results = checker.audit(system)
print(f"  Passed: {len(results['pass'])}/{len(checker.rules)}")
print(f"\n  [PASS]:")
for r in results["pass"]:
    print(f"    [{r['cat']:8s}] {r['name']}: {r['desc']}")
print(f"\n  [FAIL]:")
for r in results["fail"]:
    print(f"    [{r['cat']:8s}] {r['name']}: {r['desc']}")

print("\nDone!")
