"""
Planning and Reasoning
======================
Section 08

Demonstrates agent planning: task decomposition,
Goal-Oriented Action Planning (GOAP), and ReAct.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("PLANNING AND REASONING")
print("=" * 60)

# 1. Task Decomposition
print("\n1. TASK DECOMPOSITION")
print("-" * 40)

class TaskPlanner:
    def __init__(self):
        self.tasks = []
    def decompose(self, goal):
        self.tasks = []
        if "deploy" in goal.lower():
            self.tasks = [
                {"id": 1, "task": "Build application", "deps": []},
                {"id": 2, "task": "Run tests", "deps": [1]},
                {"id": 3, "task": "Create container", "deps": [2]},
                {"id": 4, "task": "Push to registry", "deps": [3]},
                {"id": 5, "task": "Deploy to cloud", "deps": [4]},
            ]
        elif "analyze" in goal.lower():
            self.tasks = [
                {"id": 1, "task": "Collect data", "deps": []},
                {"id": 2, "task": "Clean data", "deps": [1]},
                {"id": 3, "task": "Analyze patterns", "deps": [2]},
                {"id": 4, "task": "Generate report", "deps": [3]},
            ]
        return self.tasks

planner = TaskPlanner()
tasks = planner.decompose("Deploy AI agent to cloud")
print(f"  Goal: Deploy AI agent to cloud")
for t in tasks:
    deps = f" (after: {t['deps']})" if t['deps'] else ""
    print(f"    {t['id']}. {t['task']}{deps}")

# 2. ReAct Pattern
print("\n2. ReAct PATTERN (Reason + Act)")
print("-" * 40)

class ReActAgent:
    def __init__(self):
        self.log = []
    def step(self, thought, action, observation):
        self.log.append({"thought": thought, "action": action, "observation": observation})
    def show(self):
        for i, entry in enumerate(self.log, 1):
            print(f"  Step {i}:")
            print(f"    Thought: {entry['thought']}")
            print(f"    Action:  {entry['action']}")
            print(f"    Observe: {entry['observation']}")

agent = ReActAgent()
agent.step(
    "I need to find the population of France",
    "search('population of France')",
    "France has approximately 67 million people")
agent.step(
    "Now I need to calculate population density, need the area",
    "search('area of France')",
    "France covers 643,801 sq km")
agent.step(
    "I can now calculate: 67M / 643,801 = ~104 per sq km",
    "calculator('67000000 / 643801')",
    "104.07 people per sq km")
agent.show()

print("\nDone!")
