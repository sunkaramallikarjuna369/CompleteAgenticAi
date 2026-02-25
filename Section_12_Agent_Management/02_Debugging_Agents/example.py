"""
Debugging Agents
================
Section 12

Demonstrates debugging: step-through execution,
state inspection, and error diagnosis.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("DEBUGGING AGENTS")
print("=" * 60)

# 1. Step-Through Debugger
print("\n1. STEP-THROUGH EXECUTION")
print("-" * 40)

class AgentDebugger:
    def __init__(self):
        self.steps = []
        self.breakpoints = set()

    def add_step(self, name, state):
        self.steps.append({"name": name, "state": dict(state)})

    def set_breakpoint(self, step_name):
        self.breakpoints.add(step_name)

    def run(self):
        for i, step in enumerate(self.steps):
            is_bp = step["name"] in self.breakpoints
            marker = ">>>" if is_bp else "   "
            print(f"  {marker} Step {i+1}: {step['name']}")
            print(f"       State: {step['state']}")
            if is_bp:
                print(f"       [BREAKPOINT HIT]")

debugger = AgentDebugger()
debugger.add_step("perceive", {"input": "user query", "tokens": 15})
debugger.add_step("plan", {"subtasks": 3, "strategy": "sequential"})
debugger.add_step("retrieve", {"docs_found": 5, "relevant": 3})
debugger.add_step("generate", {"tokens_out": 150, "confidence": 0.85})
debugger.add_step("validate", {"checks_passed": True})

debugger.set_breakpoint("retrieve")
debugger.set_breakpoint("generate")
debugger.run()

# 2. Error Diagnosis
print("\n2. ERROR DIAGNOSIS")
print("-" * 40)

class ErrorDiagnoser:
    def __init__(self):
        self.patterns = {
            "timeout": {"cause": "LLM API latency", "fix": "Increase timeout or use cache"},
            "token_limit": {"cause": "Input too long", "fix": "Implement chunking strategy"},
            "hallucination": {"cause": "Weak grounding", "fix": "Add RAG or fact-checking"},
            "loop": {"cause": "Agent stuck in loop", "fix": "Add max iterations guard"},
        }

    def diagnose(self, error_type):
        info = self.patterns.get(error_type, {"cause": "Unknown", "fix": "Investigate logs"})
        return info

diagnoser = ErrorDiagnoser()
errors = ["timeout", "token_limit", "hallucination", "loop"]

for err in errors:
    info = diagnoser.diagnose(err)
    print(f"  Error: {err}")
    print(f"    Cause: {info['cause']}")
    print(f"    Fix:   {info['fix']}\n")

print("Done!")
