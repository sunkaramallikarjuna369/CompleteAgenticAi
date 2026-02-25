"""
Agent Communication
===================
Section 11

Demonstrates communication: message passing,
publish-subscribe, and blackboard patterns.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("AGENT COMMUNICATION")
print("=" * 60)

# 1. Message Passing
print("\n1. DIRECT MESSAGE PASSING")
print("-" * 40)

class MessageAgent:
    def __init__(self, name):
        self.name = name
        self.inbox = []
    def send(self, recipient, content, msg_type="INFORM"):
        msg = {"from": self.name, "type": msg_type, "content": content}
        recipient.inbox.append(msg)
        print(f"  {self.name} -> {recipient.name} [{msg_type}]: {content[:40]}")
    def read_messages(self):
        msgs = self.inbox.copy()
        self.inbox.clear()
        return msgs

alice = MessageAgent("Alice")
bob = MessageAgent("Bob")
alice.send(bob, "Can you analyze dataset X?", "REQUEST")
bob.send(alice, "Analysis complete: 95% accuracy", "INFORM")

# 2. Publish-Subscribe
print("\n2. PUBLISH-SUBSCRIBE")
print("-" * 40)

class EventBus:
    def __init__(self):
        self.subscribers = {}
    def subscribe(self, topic, agent_name):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(agent_name)
    def publish(self, topic, message):
        subs = self.subscribers.get(topic, [])
        print(f"  Published to '{topic}' ({len(subs)} subscribers):")
        for sub in subs:
            print(f"    -> {sub} received: {message[:40]}")

bus = EventBus()
bus.subscribe("task_complete", "Logger")
bus.subscribe("task_complete", "Monitor")
bus.subscribe("error", "AlertSystem")
bus.subscribe("error", "Logger")

bus.publish("task_complete", "Agent finished data analysis")
bus.publish("error", "Agent encountered timeout")

# 3. Blackboard Pattern
print("\n3. BLACKBOARD PATTERN")
print("-" * 40)

class Blackboard:
    def __init__(self):
        self.data = {}
    def write(self, agent_name, key, value):
        self.data[key] = {"value": value, "author": agent_name}
        print(f"  [{agent_name}] wrote '{key}' = {str(value)[:30]}")
    def read(self, key):
        return self.data.get(key, {}).get("value")
    def show(self):
        for key, entry in self.data.items():
            print(f"  {key}: {entry['value']} (by {entry['author']})")

bb = Blackboard()
bb.write("Researcher", "findings", "3 relevant papers found")
bb.write("Analyzer", "statistics", {"mean": 0.85, "std": 0.03})
bb.write("Writer", "draft", "AI agents are transforming...")

print("\n  Blackboard state:")
bb.show()

print("\nDone!")
