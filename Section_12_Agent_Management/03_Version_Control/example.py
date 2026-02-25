"""
Agent Version Control
=====================
Section 12

Demonstrates version control for agents: prompt versioning,
model registry, and rollback.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

from datetime import datetime

print("=" * 60)
print("AGENT VERSION CONTROL")
print("=" * 60)

# 1. Prompt Versioning
print("\n1. PROMPT VERSIONING")
print("-" * 40)

class PromptVersion:
    def __init__(self):
        self.versions = []
    def commit(self, prompt, message, metrics=None):
        version = len(self.versions) + 1
        self.versions.append({
            "version": f"v{version}.0",
            "prompt": prompt[:60],
            "message": message,
            "metrics": metrics or {},
            "date": datetime.now().isoformat(),
        })
    def history(self):
        for v in self.versions:
            metrics_str = f" metrics={v['metrics']}" if v['metrics'] else ""
            print(f"  {v['version']}: {v['message']}{metrics_str}")
    def rollback(self, version_str):
        for v in self.versions:
            if v["version"] == version_str:
                print(f"  Rolled back to {version_str}: {v['prompt'][:40]}...")
                return v
        return None

pv = PromptVersion()
pv.commit("You are a helpful AI assistant...", "Initial prompt", {"accuracy": 0.75})
pv.commit("You are an expert AI assistant. Be concise...", "Add conciseness", {"accuracy": 0.82})
pv.commit("You are an expert AI assistant. Be concise. Use examples...", "Add examples", {"accuracy": 0.89})

pv.history()
pv.rollback("v2.0")

# 2. Model Registry
print("\n2. MODEL REGISTRY")
print("-" * 40)

class ModelRegistry:
    def __init__(self):
        self.models = []
    def register(self, name, version, stage, metrics):
        self.models.append({"name": name, "version": version, "stage": stage, "metrics": metrics})
    def promote(self, name, version):
        for m in self.models:
            if m["name"] == name and m["version"] == version:
                m["stage"] = "production"
    def list_models(self):
        for m in self.models:
            print(f"  {m['name']} v{m['version']} [{m['stage']:12s}] acc={m['metrics'].get('accuracy', 'N/A')}")

registry = ModelRegistry()
registry.register("agent-v1", "1.0", "archived", {"accuracy": 0.82})
registry.register("agent-v1", "1.1", "staging", {"accuracy": 0.87})
registry.register("agent-v1", "1.2", "production", {"accuracy": 0.91})
registry.list_models()

print("\nDone!")
