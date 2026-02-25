"""
Agent Design Patterns
=====================
Section 10

Demonstrates design patterns: router, supervisor,
pipeline, and reflection patterns.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("AGENT DESIGN PATTERNS")
print("=" * 60)

# 1. Router Pattern
print("\n1. ROUTER PATTERN")
print("-" * 40)

class RouterAgent:
    def __init__(self):
        self.routes = {}
    def add_route(self, pattern, handler_name):
        self.routes[pattern] = handler_name
    def route(self, query):
        for pattern, handler in self.routes.items():
            if pattern in query.lower():
                return handler
        return "default_handler"

router = RouterAgent()
router.add_route("code", "coding_agent")
router.add_route("data", "data_agent")
router.add_route("deploy", "devops_agent")

queries = ["Write code for sorting", "Analyze the data", "Deploy to AWS", "What is AI?"]
for q in queries:
    handler = router.route(q)
    print(f"  '{q}' -> {handler}")

# 2. Supervisor Pattern
print("\n2. SUPERVISOR PATTERN")
print("-" * 40)

class Supervisor:
    def __init__(self):
        self.workers = {}
        self.results = {}
    def add_worker(self, name, capability):
        self.workers[name] = capability
    def delegate(self, task):
        for name, cap in self.workers.items():
            if cap in task.lower():
                self.results[name] = f"Completed: {task}"
                return name
        return None
    def collect_results(self):
        return self.results

sup = Supervisor()
sup.add_worker("coder", "write")
sup.add_worker("tester", "test")
sup.add_worker("reviewer", "review")

tasks = ["Write the API endpoint", "Test the login flow", "Review the pull request"]
for task in tasks:
    worker = sup.delegate(task)
    print(f"  '{task}' -> assigned to: {worker}")

# 3. Pipeline Pattern
print("\n3. PIPELINE PATTERN")
print("-" * 40)

class PipelineAgent:
    def __init__(self):
        self.stages = []
    def add_stage(self, name, func):
        self.stages.append((name, func))
    def run(self, data):
        for name, func in self.stages:
            data = func(data)
            print(f"  [{name:15s}] -> {str(data)[:40]}")
        return data

pipe = PipelineAgent()
pipe.add_stage("Intake", lambda d: {"query": d, "status": "received"})
pipe.add_stage("Classify", lambda d: {**d, "category": "technical"})
pipe.add_stage("Process", lambda d: {**d, "answer": "Here is the solution..."})
pipe.add_stage("Format", lambda d: {**d, "formatted": True})

pipe.run("How do I sort a list in Python?")

print("\nDone!")
