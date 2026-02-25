"""
Multi-Agent Architectures
=========================
Section 11

Demonstrates multi-agent architectures: centralized,
decentralized, and hierarchical systems.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("MULTI-AGENT ARCHITECTURES")
print("=" * 60)

class Agent:
    def __init__(self, name, capability):
        self.name = name
        self.capability = capability
    def process(self, task):
        return f"[{self.name}] Processed: {task}"

# 1. Centralized Architecture
print("\n1. CENTRALIZED (Hub-and-Spoke)")
print("-" * 40)

class CentralCoordinator:
    def __init__(self):
        self.agents = []
    def register(self, agent):
        self.agents.append(agent)
    def assign(self, tasks):
        results = []
        for task in tasks:
            for agent in self.agents:
                if agent.capability in task.lower():
                    result = agent.process(task)
                    results.append(result)
                    print(f"  {result}")
                    break
        return results

coord = CentralCoordinator()
coord.register(Agent("Coder", "code"))
coord.register(Agent("Tester", "test"))
coord.register(Agent("Writer", "write"))

coord.assign(["Write code for API", "Test the endpoint", "Write documentation"])

# 2. Decentralized (Peer-to-Peer)
print("\n2. DECENTRALIZED (Peer-to-Peer)")
print("-" * 40)

class PeerAgent:
    def __init__(self, name):
        self.name = name
        self.peers = []
        self.inbox = []
    def connect(self, peer):
        self.peers.append(peer)
        peer.peers.append(self)
    def broadcast(self, message):
        for peer in self.peers:
            peer.inbox.append(f"From {self.name}: {message}")
            print(f"  {self.name} -> {peer.name}: {message[:40]}")

a1 = PeerAgent("Agent-A")
a2 = PeerAgent("Agent-B")
a3 = PeerAgent("Agent-C")
a1.connect(a2)
a1.connect(a3)

a1.broadcast("I found relevant data")
a2.broadcast("Processing complete")

# 3. Hierarchical
print("\n3. HIERARCHICAL")
print("-" * 40)

class HierarchicalAgent:
    def __init__(self, name, level):
        self.name = name
        self.level = level  # 0=top, 1=mid, 2=worker
        self.subordinates = []
    def add_subordinate(self, agent):
        self.subordinates.append(agent)
    def delegate(self, task, indent=0):
        prefix = "  " * indent
        print(f"{prefix}  [{self.name} L{self.level}] {task}")
        if self.subordinates:
            subtasks = [f"Subtask-{i+1} of '{task[:20]}'" for i in range(len(self.subordinates))]
            for sub, subtask in zip(self.subordinates, subtasks):
                sub.delegate(subtask, indent + 1)

director = HierarchicalAgent("Director", 0)
manager1 = HierarchicalAgent("Manager-A", 1)
manager2 = HierarchicalAgent("Manager-B", 1)
worker1 = HierarchicalAgent("Worker-1", 2)
worker2 = HierarchicalAgent("Worker-2", 2)
worker3 = HierarchicalAgent("Worker-3", 2)

director.add_subordinate(manager1)
director.add_subordinate(manager2)
manager1.add_subordinate(worker1)
manager1.add_subordinate(worker2)
manager2.add_subordinate(worker3)

director.delegate("Build AI Agent System")

print("\nDone!")
