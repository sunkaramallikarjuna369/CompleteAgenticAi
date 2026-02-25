"""
Building Your Career in Agentic AI
==================================
Section 16

Explores career paths, skills, and resources
for agentic AI professionals.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("BUILDING YOUR CAREER IN AGENTIC AI")
print("=" * 60)

# 1. Career Paths
print("\n1. CAREER PATHS")
print("-" * 40)

careers = [
    ("AI/ML Engineer", ["Python", "PyTorch/TF", "MLOps", "Cloud"], "$$$$"),
    ("AI Agent Developer", ["LangChain", "RAG", "Prompt Eng", "APIs"], "$$$$"),
    ("AI Architect", ["System Design", "Cloud", "Security", "Scale"], "$$$$$"),
    ("AI Researcher", ["Math", "Papers", "Experiments", "Publishing"], "$$$$"),
    ("AI Product Manager", ["Strategy", "UX", "Business", "Ethics"], "$$$$"),
]

print(f"  {'Role':25s} {'Key Skills':45s} {'Pay'}")
for role, skills, pay in careers:
    print(f"  {role:25s} {', '.join(skills):45s} {pay}")

# 2. Learning Roadmap
print("\n2. LEARNING ROADMAP")
print("-" * 40)

roadmap = [
    ("Month 1-2", "Python + ML basics + math foundations"),
    ("Month 3-4", "Deep learning + NLP + transformers"),
    ("Month 5-6", "LLMs + prompt engineering + RAG"),
    ("Month 7-8", "Agent frameworks + multi-agent systems"),
    ("Month 9-10", "Cloud deployment + MLOps + production"),
    ("Month 11-12", "Portfolio projects + open source + networking"),
]

for period, focus in roadmap:
    print(f"  {period:12s}: {focus}")

# 3. Resources
print("\n3. KEY RESOURCES")
print("-" * 40)

resources = [
    ("Papers", "arxiv.org - Read foundational papers"),
    ("Code", "GitHub - Contribute to open source"),
    ("Community", "Discord/Reddit - Join AI communities"),
    ("Practice", "Kaggle/HuggingFace - Build projects"),
    ("Certifications", "AWS/Azure/GCP AI certifications"),
]

for category, desc in resources:
    print(f"  {category:15s}: {desc}")

print("\n  KEY TAKEAWAY: Start building, keep learning,")
print("  contribute to open source, and never stop experimenting!")

print("\nDone!")
