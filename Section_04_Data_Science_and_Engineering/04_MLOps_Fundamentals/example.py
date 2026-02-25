"""
MLOps Fundamentals
==================
Section 04

Demonstrates MLOps: experiment tracking, model versioning,
and monitoring.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import json, random
from datetime import datetime

print("=" * 60)
print("1. EXPERIMENT TRACKING")
print("=" * 60)

class ExperimentTracker:
    def __init__(self):
        self.experiments = []
    def log(self, name, params, metrics):
        self.experiments.append({"name": name, "params": params, "metrics": metrics,
                                 "timestamp": datetime.now().isoformat()})
    def best(self, metric="accuracy"):
        return max(self.experiments, key=lambda e: e["metrics"].get(metric, 0))

tracker = ExperimentTracker()
random.seed(42)
for i in range(5):
    lr = random.choice([0.001, 0.01, 0.1])
    acc = 0.7 + random.random() * 0.25
    tracker.log(f"exp_{i}", {"lr": lr, "epochs": (i+1)*10}, {"accuracy": round(acc, 3), "loss": round(1-acc, 3)})

for exp in tracker.experiments:
    print(f"  {exp['name']}: lr={exp['params']['lr']}, acc={exp['metrics']['accuracy']}")

best = tracker.best("accuracy")
print(f"\n  Best: {best['name']} ({best['metrics']['accuracy']})")

print("\n" + "=" * 60)
print("2. MODEL VERSIONING")
print("=" * 60)

class ModelRegistry:
    def __init__(self):
        self.versions = []
    def register(self, name, version, metrics, stage="staging"):
        self.versions.append({"name": name, "version": version, "metrics": metrics, "stage": stage})
    def promote(self, name, version):
        for v in self.versions:
            if v["name"] == name and v["version"] == version:
                v["stage"] = "production"

registry = ModelRegistry()
registry.register("sentiment-model", "1.0", {"accuracy": 0.88})
registry.register("sentiment-model", "1.1", {"accuracy": 0.91})
registry.register("sentiment-model", "1.2", {"accuracy": 0.93})
registry.promote("sentiment-model", "1.2")

for v in registry.versions:
    print(f"  v{v['version']}: acc={v['metrics']['accuracy']} [{v['stage']}]")

print("\nDone!")
