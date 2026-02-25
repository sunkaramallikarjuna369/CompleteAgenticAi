"""
Action Execution
================
Section 08

Demonstrates agent action execution: action planning,
execution engine, and error handling.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("ACTION EXECUTION")
print("=" * 60)

class ActionExecutor:
    def __init__(self):
        self.actions = {}
        self.history = []

    def register(self, name, handler):
        self.actions[name] = handler

    def execute(self, name, params=None):
        if name not in self.actions:
            return {"status": "error", "message": f"Unknown action: {name}"}
        try:
            result = self.actions[name](params or {})
            self.history.append({"action": name, "status": "success", "result": result})
            return {"status": "success", "result": result}
        except Exception as e:
            self.history.append({"action": name, "status": "error", "error": str(e)})
            return {"status": "error", "message": str(e)}

executor = ActionExecutor()

executor.register("search", lambda p: f"Found {random.randint(1,10)} results for '{p.get('query', '')}'")
executor.register("calculate", lambda p: eval(p.get("expression", "0")))
executor.register("format", lambda p: p.get("text", "").upper())

# Execute a plan
print("  Executing action plan:")
plan = [
    ("search", {"query": "AI agents"}),
    ("calculate", {"expression": "42 * 3 + 7"}),
    ("format", {"text": "hello world"}),
    ("unknown_action", {}),
]

random.seed(42)
for name, params in plan:
    result = executor.execute(name, params)
    status = result["status"]
    output = result.get("result", result.get("message", ""))
    print(f"  [{status:7s}] {name}({params}) -> {output}")

print(f"\n  Execution history: {len(executor.history)} actions")
success = sum(1 for h in executor.history if h["status"] == "success")
print(f"  Success rate: {success}/{len(executor.history)}")

print("\nDone!")
