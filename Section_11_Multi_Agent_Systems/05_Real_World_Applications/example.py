"""
Real-World Multi-Agent Applications
===================================
Section 11

Demonstrates real-world multi-agent applications:
software development, customer support, research.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("REAL-WORLD MULTI-AGENT APPLICATIONS")
print("=" * 60)

# 1. Software Development Team
print("\n1. SOFTWARE DEVELOPMENT TEAM")
print("-" * 40)

class DevTeamAgent:
    def __init__(self, role, tasks):
        self.role = role
        self.tasks = tasks
    def work(self):
        results = []
        for task in self.tasks:
            results.append(f"[{self.role}] {task} -> Done")
        return results

team = [
    DevTeamAgent("Product Manager", ["Define requirements", "Prioritize backlog"]),
    DevTeamAgent("Architect", ["Design system", "Choose tech stack"]),
    DevTeamAgent("Developer", ["Write code", "Fix bugs"]),
    DevTeamAgent("Tester", ["Write tests", "Run QA"]),
    DevTeamAgent("DevOps", ["Set up CI/CD", "Deploy to cloud"]),
]

print("  Sprint simulation:")
for agent in team:
    for result in agent.work():
        print(f"  {result}")

# 2. Customer Support
print("\n2. CUSTOMER SUPPORT SYSTEM")
print("-" * 40)

class SupportSystem:
    def __init__(self):
        self.agents = {
            "triage": lambda q: "billing" if "bill" in q else "technical" if "error" in q else "general",
            "billing": lambda q: "Your billing issue has been resolved",
            "technical": lambda q: "Here's the technical solution...",
            "general": lambda q: "Let me help you with that",
        }

    def handle(self, query):
        category = self.agents["triage"](query.lower())
        response = self.agents[category](query)
        return category, response

support = SupportSystem()
queries = [
    "I have a billing issue with my subscription",
    "I'm getting an error when running the agent",
    "How do I get started with the platform?",
]

for query in queries:
    cat, response = support.handle(query)
    print(f"  Query: {query[:45]}...")
    print(f"  Route: {cat} -> {response}\n")

# 3. Research Pipeline
print("3. RESEARCH PIPELINE")
print("-" * 40)

stages = [
    ("Literature Review", "Found 15 relevant papers"),
    ("Data Collection", "Gathered 10,000 data points"),
    ("Analysis", "Statistical significance p<0.05"),
    ("Writing", "Draft paper: 8 pages"),
    ("Peer Review", "2 minor revisions requested"),
]

for stage, result in stages:
    print(f"  [{stage:20s}] -> {result}")

print("\nDone!")
