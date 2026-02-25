"""
Containerization
================
Section 15

Demonstrates Docker and Kubernetes for AI agents.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("CONTAINERIZATION: DOCKER & K8S")
print("=" * 60)

# Dockerfile
print("\n1. DOCKERFILE")
print("-" * 40)

class DockerfileBuilder:
    def __init__(self):
        self.lines = []
    def add(self, instruction):
        self.lines.append(instruction)
        return self
    def build(self):
        return "\n".join(self.lines)

df = DockerfileBuilder()
df.add("FROM python:3.11-slim")
df.add("WORKDIR /app")
df.add("COPY requirements.txt .")
df.add("RUN pip install --no-cache-dir -r requirements.txt")
df.add("COPY . .")
df.add("EXPOSE 8000")
df.add('CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]')

print("  Generated Dockerfile:")
for line in df.build().split("\n"):
    print(f"    {line}")

# K8s Manifest
print("\n2. KUBERNETES DEPLOYMENT")
print("-" * 40)

manifest = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-agent
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-agent
  template:
    spec:
      containers:
      - name: agent
        image: gcr.io/project/agent:v1
        ports:
        - containerPort: 8000
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m" """

for line in manifest.strip().split("\n"):
    print(f"    {line}")

print("\nDone!")
