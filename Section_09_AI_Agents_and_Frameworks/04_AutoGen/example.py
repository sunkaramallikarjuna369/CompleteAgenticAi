"""
AutoGen Framework
=================
Section 09

Demonstrates AutoGen concepts: conversable agents,
multi-agent chat, and group conversations.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("AUTOGEN CONCEPTS")
print("=" * 60)

class ConversableAgent:
    def __init__(self, name, system_message=""):
        self.name = name
        self.system_message = system_message
        self.chat_history = []
    def receive(self, message, sender):
        self.chat_history.append({"from": sender.name, "content": message})
        response = self.generate_reply(message)
        return response
    def generate_reply(self, message):
        if "code" in message.lower():
            return f"[{self.name}] Here's the code solution..."
        elif "review" in message.lower():
            return f"[{self.name}] I've reviewed the code. Looks good!"
        return f"[{self.name}] I understand. Let me help with that."

class GroupChat:
    def __init__(self, agents, max_rounds=5):
        self.agents = agents
        self.max_rounds = max_rounds
        self.messages = []
    def run(self, initial_message, sender):
        self.messages.append({"from": sender.name, "content": initial_message})
        print(f"  [{sender.name}] {initial_message}")
        for round_num in range(self.max_rounds):
            for agent in self.agents:
                if agent != sender:
                    reply = agent.receive(self.messages[-1]["content"], sender)
                    self.messages.append({"from": agent.name, "content": reply})
                    print(f"  {reply}")
            if round_num >= 1:
                break
        return self.messages

# Create agents
user = ConversableAgent("User", "I need help with coding tasks")
coder = ConversableAgent("Coder", "I write Python code")
reviewer = ConversableAgent("Reviewer", "I review code for quality")

print("  Agents:")
for a in [user, coder, reviewer]:
    print(f"    {a.name:10s}: {a.system_message}")

print("\n  Group Chat:")
chat = GroupChat([user, coder, reviewer], max_rounds=2)
chat.run("Write a function to sort a list and review it", user)

print(f"\n  Total messages: {len(chat.messages)}")

print("\nDone!")
