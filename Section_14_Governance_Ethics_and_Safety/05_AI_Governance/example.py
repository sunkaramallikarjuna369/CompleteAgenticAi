"""
AI Governance
=============
Section 14

Demonstrates AI governance: policy frameworks,
risk assessment, and governance boards.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("AI GOVERNANCE")
print("=" * 60)

# 1. Governance Framework
print("\n1. GOVERNANCE FRAMEWORK")
print("-" * 40)

framework = {
    "Strategy": ["Define AI vision", "Align with business goals", "Set ethical boundaries"],
    "Policies": ["Data usage policy", "Model deployment policy", "Incident response"],
    "Oversight": ["Governance board", "Regular audits", "Stakeholder reporting"],
    "Compliance": ["Regulatory mapping", "Risk assessment", "Documentation"],
}

for pillar, items in framework.items():
    print(f"\n  {pillar}:")
    for item in items:
        print(f"    - {item}")

# 2. Risk Assessment
print("\n2. AI RISK ASSESSMENT")
print("-" * 40)

risks = [
    ("Bias in decisions", "High", "Medium", "Implement fairness testing"),
    ("Data breach", "Critical", "Low", "Encryption + access controls"),
    ("Model hallucination", "High", "High", "Add RAG + fact-checking"),
    ("Regulatory violation", "Critical", "Low", "Compliance monitoring"),
    ("System downtime", "Medium", "Medium", "Redundancy + monitoring"),
]

print(f"  {'Risk':25s} {'Impact':>10} {'Likelihood':>12} Mitigation")
for risk, impact, likelihood, mitigation in risks:
    print(f"  {risk:25s} {impact:>10} {likelihood:>12} {mitigation}")

print("\nDone!")
