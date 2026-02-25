"""
Agent Orchestration
===================
Section 10

Demonstrates orchestration: sequential, parallel,
and conditional agent execution.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("AGENT ORCHESTRATION")
print("=" * 60)

class OrchestratedAgent:
    def __init__(self, name, process_time=1):
        self.name = name
        self.process_time = process_time
    def execute(self, task):
        return {"agent": self.name, "task": task, "status": "done"}

class Orchestrator:
    def __init__(self):
        self.agents = {}
    def register(self, agent):
        self.agents[agent.name] = agent

    def sequential(self, tasks):
        print("  Sequential Execution:")
        results = []
        for task in tasks:
            agent_name = task["agent"]
            agent = self.agents[agent_name]
            result = agent.execute(task["task"])
            results.append(result)
            print(f"    [{agent_name}] {task['task']} -> {result['status']}")
        return results

    def parallel(self, tasks):
        print("  Parallel Execution:")
        results = []
        for task in tasks:
            agent_name = task["agent"]
            agent = self.agents[agent_name]
            result = agent.execute(task["task"])
            results.append(result)
        for r in results:
            print(f"    [{r['agent']}] {r['task']} -> {r['status']}")
        return results

    def conditional(self, task, condition_fn):
        print("  Conditional Execution:")
        if condition_fn():
            return self.agents[task["agent"]].execute(task["task"])
        print(f"    Skipped: {task['task']} (condition not met)")
        return None

orch = Orchestrator()
orch.register(OrchestratedAgent("researcher"))
orch.register(OrchestratedAgent("writer"))
orch.register(OrchestratedAgent("reviewer"))

# Sequential
orch.sequential([
    {"agent": "researcher", "task": "Research AI trends"},
    {"agent": "writer", "task": "Write article"},
    {"agent": "reviewer", "task": "Review article"},
])

# Parallel
print()
orch.parallel([
    {"agent": "researcher", "task": "Research topic A"},
    {"agent": "writer", "task": "Draft introduction"},
])

# Conditional
print()
random.seed(42)
orch.conditional(
    {"agent": "reviewer", "task": "Final review"},
    lambda: random.random() > 0.3
)

print("\nDone!")
