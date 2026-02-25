"""
Agent Protocols
===============
Section 09

Demonstrates agent communication protocols:
message formats, handshakes, and standards.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import json

print("=" * 60)
print("AGENT PROTOCOLS")
print("=" * 60)

class AgentMessage:
    def __init__(self, sender, receiver, performative, content):
        self.sender = sender
        self.receiver = receiver
        self.performative = performative  # REQUEST, INFORM, AGREE, REFUSE
        self.content = content
    def to_dict(self):
        return {"sender": self.sender, "receiver": self.receiver,
                "performative": self.performative, "content": self.content}
    def __repr__(self):
        return f"[{self.performative}] {self.sender} -> {self.receiver}: {self.content}"

class ProtocolAgent:
    def __init__(self, name):
        self.name = name
        self.inbox = []
    def send(self, receiver, performative, content):
        msg = AgentMessage(self.name, receiver.name, performative, content)
        receiver.inbox.append(msg)
        return msg
    def process_inbox(self):
        responses = []
        for msg in self.inbox:
            if msg.performative == "REQUEST":
                response = AgentMessage(self.name, msg.sender, "AGREE", f"Will do: {msg.content}")
            elif msg.performative == "INFORM":
                response = AgentMessage(self.name, msg.sender, "INFORM", "Acknowledged")
            else:
                response = AgentMessage(self.name, msg.sender, "INFORM", "OK")
            responses.append(response)
        self.inbox.clear()
        return responses

# Protocol demonstration
print("\n  AGENT COMMUNICATION PROTOCOL")
print("-" * 40)

coordinator = ProtocolAgent("Coordinator")
worker1 = ProtocolAgent("Worker-1")
worker2 = ProtocolAgent("Worker-2")

# Coordinator sends tasks
msg1 = coordinator.send(worker1, "REQUEST", "Analyze dataset A")
msg2 = coordinator.send(worker2, "REQUEST", "Analyze dataset B")
print(f"  {msg1}")
print(f"  {msg2}")

# Workers process
print("\n  Worker responses:")
for worker in [worker1, worker2]:
    responses = worker.process_inbox()
    for r in responses:
        print(f"  {r}")

# Workers report back
worker1.send(coordinator, "INFORM", "Analysis complete: 95% accuracy")
worker2.send(coordinator, "INFORM", "Analysis complete: 92% accuracy")

print("\n  Coordinator inbox:")
for msg in coordinator.inbox:
    print(f"  {msg}")

print("\nDone!")
