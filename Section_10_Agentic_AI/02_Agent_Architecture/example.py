"""
Agent Architecture
==================
Section 10

Demonstrates agent architectures: reactive, deliberative,
hybrid, and BDI agents.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("AGENT ARCHITECTURES")
print("=" * 60)

# 1. Reactive Agent
print("\n1. REACTIVE AGENT")
print("-" * 40)

class ReactiveAgent:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition, action):
        self.rules.append((condition, action))
    def act(self, percept):
        for cond, action in self.rules:
            if cond(percept):
                return action
        return "do_nothing"

reactive = ReactiveAgent()
reactive.add_rule(lambda p: p.get("obstacle"), "avoid")
reactive.add_rule(lambda p: p.get("goal_visible"), "move_to_goal")
reactive.add_rule(lambda p: True, "explore")

for percept in [{"obstacle": True}, {"goal_visible": True}, {}]:
    action = reactive.act(percept)
    print(f"  {percept} -> {action}")

# 2. BDI Agent (Beliefs-Desires-Intentions)
print("\n2. BDI AGENT")
print("-" * 40)

class BDIAgent:
    def __init__(self):
        self.beliefs = {}
        self.desires = []
        self.intentions = []

    def update_beliefs(self, percepts):
        self.beliefs.update(percepts)

    def generate_desires(self):
        self.desires = []
        if self.beliefs.get("task_pending"):
            self.desires.append("complete_task")
        if self.beliefs.get("low_battery"):
            self.desires.append("recharge")
        if self.beliefs.get("new_data"):
            self.desires.append("process_data")

    def select_intention(self):
        priority = {"recharge": 3, "complete_task": 2, "process_data": 1}
        if self.desires:
            self.intentions = sorted(self.desires, key=lambda d: -priority.get(d, 0))
        return self.intentions[0] if self.intentions else None

    def execute(self):
        self.generate_desires()
        intention = self.select_intention()
        return intention

bdi = BDIAgent()
bdi.update_beliefs({"task_pending": True, "low_battery": True, "new_data": True})

print(f"  Beliefs: {bdi.beliefs}")
action = bdi.execute()
print(f"  Desires: {bdi.desires}")
print(f"  Intentions: {bdi.intentions}")
print(f"  Selected: {action}")

# 3. Hybrid Architecture
print("\n3. HYBRID ARCHITECTURE")
print("-" * 40)

class HybridAgent:
    def __init__(self):
        self.reactive_layer = ReactiveAgent()
        self.reactive_layer.add_rule(lambda p: p.get("urgent"), "handle_urgent")

    def process(self, percept):
        # Reactive layer first
        reactive_action = self.reactive_layer.act(percept)
        if reactive_action != "do_nothing":
            return f"REACTIVE: {reactive_action}"
        # Deliberative layer
        return f"DELIBERATIVE: plan_and_execute"

hybrid = HybridAgent()
for p in [{"urgent": True}, {"task": "analyze"}]:
    result = hybrid.process(p)
    print(f"  {p} -> {result}")

print("\nDone!")
