"""
CI/CD for AI
============
Section 15

Demonstrates CI/CD pipelines for AI systems.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("CI/CD FOR AI SYSTEMS")
print("=" * 60)

class Pipeline:
    def __init__(self, name):
        self.name = name
        self.stages = []
    def add_stage(self, name, steps):
        self.stages.append({"name": name, "steps": steps})
    def run(self):
        print(f"  Pipeline: {self.name}")
        for stage in self.stages:
            print(f"\n  Stage: {stage['name']}")
            for step in stage["steps"]:
                print(f"    [OK] {step}")
        print(f"\n  Pipeline: PASSED")

pipeline = Pipeline("AI Agent CI/CD")
pipeline.add_stage("Build", [
    "Checkout code",
    "Install dependencies",
    "Build Docker image",
    "Run linting",
])
pipeline.add_stage("Test", [
    "Unit tests",
    "Integration tests",
    "Model accuracy check (>= 0.90)",
    "Security scan",
])
pipeline.add_stage("Deploy", [
    "Push to registry",
    "Deploy to staging",
    "Run smoke tests",
    "Blue-green deploy to production",
])

pipeline.run()

# GitHub Actions
print("\n" + "=" * 60)
print("GITHUB ACTIONS WORKFLOW")
print("=" * 60)

yaml = """name: AI Agent CI/CD
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: pytest tests/

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - run: echo 'Deploying...'"""

for line in yaml.split("\n"):
    print(f"  {line}")

print("\nDone!")
