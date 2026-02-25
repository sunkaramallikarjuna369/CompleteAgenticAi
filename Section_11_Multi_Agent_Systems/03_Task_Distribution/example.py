"""
Task Distribution
=================
Section 11

Demonstrates task distribution: round-robin,
capability-based, and load-balanced allocation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("TASK DISTRIBUTION")
print("=" * 60)

class Worker:
    def __init__(self, name, capabilities, load=0):
        self.name = name
        self.capabilities = capabilities
        self.load = load
        self.tasks = []

workers = [
    Worker("W1", ["code", "test"], 2),
    Worker("W2", ["code", "deploy"], 5),
    Worker("W3", ["test", "review"], 1),
    Worker("W4", ["deploy", "monitor"], 3),
]

tasks = ["code API", "test endpoint", "deploy service", "code frontend",
         "review PR", "test integration", "monitor logs", "code backend"]

# 1. Round Robin
print("\n1. ROUND ROBIN")
print("-" * 40)

def round_robin(tasks, workers):
    assignments = []
    for i, task in enumerate(tasks):
        w = workers[i % len(workers)]
        assignments.append((task, w.name))
        print(f"  {task:20s} -> {w.name}")
    return assignments

round_robin(tasks, workers)

# 2. Capability-Based
print("\n2. CAPABILITY-BASED")
print("-" * 40)

def capability_based(tasks, workers):
    for task in tasks:
        task_type = task.split()[0]
        candidates = [w for w in workers if task_type in w.capabilities]
        if candidates:
            chosen = candidates[0]
            print(f"  {task:20s} -> {chosen.name} (has '{task_type}')")
        else:
            print(f"  {task:20s} -> UNASSIGNED (no capable worker)")

capability_based(tasks, workers)

# 3. Load-Balanced
print("\n3. LOAD-BALANCED")
print("-" * 40)

def load_balanced(tasks, workers):
    for task in tasks:
        task_type = task.split()[0]
        candidates = [w for w in workers if task_type in w.capabilities]
        if not candidates:
            candidates = workers
        chosen = min(candidates, key=lambda w: w.load)
        chosen.load += 1
        chosen.tasks.append(task)
        print(f"  {task:20s} -> {chosen.name} (load={chosen.load})")

# Reset loads
for w in workers:
    w.load = 0
    w.tasks = []

load_balanced(tasks, workers)

print("\n  Final loads:")
for w in workers:
    bar = "#" * w.load
    print(f"    {w.name}: {bar} ({w.load} tasks)")

print("\nDone!")
