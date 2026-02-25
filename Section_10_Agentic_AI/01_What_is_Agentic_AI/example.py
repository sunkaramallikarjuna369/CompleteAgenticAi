"""
What is Agentic AI
==================
Section 10

Demonstrates agentic AI concepts: autonomy levels,
architectures, and agent lifecycle.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("WHAT IS AGENTIC AI")
print("=" * 60)

# 1. Autonomy Levels
print("\n1. AUTONOMY LEVELS")
print("-" * 40)

autonomy_levels = [
    (1, "Assistive", "Responds to explicit commands only"),
    (2, "Suggestive", "Proactively offers suggestions"),
    (3, "Semi-autonomous", "Makes decisions with human approval"),
    (4, "Autonomous", "Acts independently within boundaries"),
    (5, "Fully autonomous", "Self-directed goal pursuit"),
]

for level, name, desc in autonomy_levels:
    bar = "#" * (level * 6)
    print(f"  L{level} {name:18s}: {bar} {desc}")

# 2. Agent Architecture
print("\n2. AGENT ARCHITECTURE")
print("-" * 40)

class AgenticSystem:
    def __init__(self, name, autonomy_level):
        self.name = name
        self.autonomy = autonomy_level
        self.components = []

    def add_component(self, name, description):
        self.components.append({"name": name, "desc": description})

    def describe(self):
        print(f"  Agent: {self.name} (Autonomy Level: {self.autonomy})")
        for c in self.components:
            print(f"    [{c['name']:15s}] {c['desc']}")

agent = AgenticSystem("Research Assistant", 3)
agent.add_component("Perception", "Processes user input and context")
agent.add_component("Planning", "Decomposes goals into subtasks")
agent.add_component("Reasoning", "Applies logic and knowledge")
agent.add_component("Memory", "Stores and retrieves information")
agent.add_component("Action", "Executes tools and generates output")
agent.add_component("Reflection", "Evaluates and improves performance")
agent.describe()

# 3. Agent Loop
print("\n3. AGENT LOOP (Perceive -> Plan -> Act)")
print("-" * 40)

class AgentLoop:
    def __init__(self):
        self.state = "idle"
    def run(self, goal, max_steps=5):
        self.state = "running"
        for step in range(1, max_steps+1):
            perception = f"Step {step}: Observing environment"
            plan = f"Step {step}: Planning next action"
            action = f"Step {step}: Executing action"
            print(f"  {perception}")
            print(f"  {plan}")
            print(f"  {action}")
            if step >= 3:
                print(f"  Step {step}: Goal achieved!")
                self.state = "done"
                break
        return self.state

loop = AgentLoop()
status = loop.run("Complete the research task")
print(f"  Final state: {status}")

print("\nDone!")
