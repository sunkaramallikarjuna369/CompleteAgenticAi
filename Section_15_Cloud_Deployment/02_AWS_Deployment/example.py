"""
AWS Deployment
==============
Section 15

Demonstrates AWS deployment patterns for AI agents.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import json

print("=" * 60)
print("AWS DEPLOYMENT FOR AI AGENTS")
print("=" * 60)

class AWSArchitecture:
    def __init__(self, name):
        self.name = name
        self.services = []
    def add(self, service, purpose, config=""):
        self.services.append({"service": service, "purpose": purpose, "config": config})
    def display(self):
        print(f"\n  Architecture: {self.name}")
        for s in self.services:
            cfg = f" ({s['config']})" if s['config'] else ""
            print(f"    {s['service']:25s}: {s['purpose']}{cfg}")

arch = AWSArchitecture("AI Agent Platform")
arch.add("API Gateway", "REST API entry", "throttle: 1000/s")
arch.add("Lambda", "Agent logic", "1024MB")
arch.add("ECS Fargate", "Long-running tasks", "2 vCPU")
arch.add("DynamoDB", "Agent state/memory", "on-demand")
arch.add("S3", "Document storage")
arch.add("OpenSearch", "Vector search")
arch.add("CloudWatch", "Monitoring")

arch.display()

print("\n  Sample IAM Policy:")
policy = {"Version": "2012-10-17", "Statement": [
    {"Effect": "Allow", "Action": ["dynamodb:GetItem", "dynamodb:PutItem"],
     "Resource": "arn:aws:dynamodb:*:*:table/agent-*"}]}
print(f"  {json.dumps(policy, indent=2)[:150]}...")

print("\nDone!")
