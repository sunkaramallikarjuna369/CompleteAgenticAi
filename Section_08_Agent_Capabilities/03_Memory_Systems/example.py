"""
Memory Systems
==============
Section 08

Demonstrates agent memory: short-term, long-term,
episodic, and conversation memory.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

from collections import deque
import json

print("=" * 60)
print("AGENT MEMORY SYSTEMS")
print("=" * 60)

# 1. Short-term Memory (Buffer)
print("\n1. SHORT-TERM MEMORY")
print("-" * 40)

class ShortTermMemory:
    def __init__(self, capacity=5):
        self.buffer = deque(maxlen=capacity)
    def add(self, item):
        self.buffer.append(item)
    def get_recent(self, n=3):
        return list(self.buffer)[-n:]
    def search(self, keyword):
        return [item for item in self.buffer if keyword.lower() in str(item).lower()]

stm = ShortTermMemory(5)
for msg in ["Hello", "How does RAG work?", "It uses retrieval", "Show me an example", "Thanks!", "Bye!"]:
    stm.add(msg)
print(f"  Buffer (cap=5): {list(stm.buffer)}")
print(f"  Recent 3: {stm.get_recent(3)}")

# 2. Long-term Memory
print("\n2. LONG-TERM MEMORY")
print("-" * 40)

class LongTermMemory:
    def __init__(self):
        self.store = {}
    def save(self, key, value, importance=1.0):
        self.store[key] = {"value": value, "importance": importance, "access_count": 0}
    def recall(self, key):
        if key in self.store:
            self.store[key]["access_count"] += 1
            return self.store[key]["value"]
        return None
    def get_important(self, threshold=0.5):
        return {k: v["value"] for k, v in self.store.items() if v["importance"] >= threshold}

ltm = LongTermMemory()
ltm.save("user_name", "Alice", 0.9)
ltm.save("preference_language", "Python", 0.8)
ltm.save("last_topic", "RAG", 0.3)
ltm.save("expertise_level", "advanced", 0.7)

print(f"  All memories: {len(ltm.store)}")
print(f"  Important (>0.5): {ltm.get_important(0.5)}")
print(f"  Recall 'user_name': {ltm.recall('user_name')}")

# 3. Conversation Memory
print("\n3. CONVERSATION MEMORY")
print("-" * 40)

class ConversationMemory:
    def __init__(self, max_turns=10):
        self.history = deque(maxlen=max_turns)
        self.summary = ""
    def add_turn(self, role, content):
        self.history.append({"role": role, "content": content})
    def get_context(self, last_n=3):
        return list(self.history)[-last_n:]
    def get_full(self):
        return list(self.history)

conv = ConversationMemory(10)
conv.add_turn("user", "What is RAG?")
conv.add_turn("assistant", "RAG is Retrieval-Augmented Generation...")
conv.add_turn("user", "How does it compare to fine-tuning?")
conv.add_turn("assistant", "RAG retrieves at inference time, fine-tuning adapts weights...")

for turn in conv.get_context(4):
    print(f"  [{turn['role']:10s}] {turn['content'][:50]}")

print("\nDone!")
