"""
Serverless AI
=============
Section 15

Demonstrates serverless patterns for AI workloads.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("SERVERLESS AI")
print("=" * 60)

class ServerlessFunction:
    def __init__(self, name, memory_mb=256, timeout_s=30):
        self.name = name
        self.memory = memory_mb
        self.timeout = timeout_s
        self.invocations = 0
    def invoke(self, event):
        self.invocations += 1
        return {"status": "ok", "function": self.name, "event": str(event)[:30]}
    def cost(self, invocations, avg_duration_ms=200):
        gb_seconds = (self.memory / 1024) * (avg_duration_ms / 1000) * invocations
        return gb_seconds * 0.0000166667  # AWS Lambda pricing

# Define serverless functions
functions = [
    ServerlessFunction("agent-router", 256, 10),
    ServerlessFunction("llm-processor", 1024, 60),
    ServerlessFunction("rag-retriever", 512, 15),
    ServerlessFunction("response-formatter", 256, 5),
]

print("  Serverless Functions:")
for f in functions:
    monthly_cost = f.cost(100000)
    print(f"  {f.name:20s} {f.memory}MB  {f.timeout}s timeout  ${monthly_cost:.2f}/100k invocations")

# Event-driven pipeline
print("\n  Event-Driven Pipeline:")
event = {"query": "How does RAG work?", "user": "alice"}
for f in functions:
    result = f.invoke(event)
    print(f"    {f.name} -> {result['status']}")

total_cost = sum(f.cost(100000) for f in functions)
print(f"\n  Total monthly cost (100k req): ${total_cost:.2f}")

print("\nDone!")
