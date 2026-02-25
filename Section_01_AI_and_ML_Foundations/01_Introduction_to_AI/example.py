"""
Introduction to AI
==================
Section 01

Demonstrates core AI concepts: rule-based systems,
reactive agents, and search algorithms.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("1. RULE-BASED AI SYSTEM")
print("=" * 60)

class RuleBasedAI:
    def __init__(self):
        self.rules = []
    def add_rule(self, condition, action):
        self.rules.append((condition, action))
    def evaluate(self, facts):
        for cond, act in self.rules:
            if cond(facts):
                return act(facts)
        return "No rule matched"

ai = RuleBasedAI()
ai.add_rule(lambda f: f.get("temp", 0) > 30, lambda f: f"Turn on AC (temp={f['temp']}C)")
ai.add_rule(lambda f: f.get("temp", 0) < 15, lambda f: f"Turn on heater (temp={f['temp']}C)")
ai.add_rule(lambda f: True, lambda f: f"Temperature OK ({f['temp']}C)")

for temp in [35, 10, 22]:
    print(f"  {ai.evaluate({'temp': temp})}")

print("\n" + "=" * 60)
print("2. REACTIVE AGENT")
print("=" * 60)

class ReactiveAgent:
    def __init__(self, name):
        self.name = name
    def perceive_and_act(self, env):
        if env.get("obstacle"):
            return "avoid"
        elif env.get("target"):
            return "move_toward_target"
        return "explore"

agent = ReactiveAgent("Bot")
envs = [{"obstacle": True}, {"target": True}, {}]
for e in envs:
    print(f"  Env={e} -> Action: {agent.perceive_and_act(e)}")

print("\n" + "=" * 60)
print("3. BFS SEARCH")
print("=" * 60)

from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
path = bfs(graph, "A", "F")
print(f"  Path A->F: {' -> '.join(path)}")

print("\n" + "=" * 60)
print("4. AI TYPES OVERVIEW")
print("=" * 60)
types = [
    ("Narrow AI", "Task-specific", "Chess engines, Siri"),
    ("General AI", "Human-level reasoning", "Theoretical"),
    ("Super AI", "Beyond human capability", "Hypothetical"),
]
for name, desc, ex in types:
    print(f"  {name:12s}: {desc:28s} e.g. {ex}")

print("\nDone!")
