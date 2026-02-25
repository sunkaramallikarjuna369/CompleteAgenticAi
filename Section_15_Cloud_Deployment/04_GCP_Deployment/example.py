"""
GCP Deployment
==============
Section 15

Demonstrates Google Cloud deployment for AI agents.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("GCP DEPLOYMENT FOR AI AGENTS")
print("=" * 60)

services = [
    ("Cloud Run", "Managed", "Agent API"),
    ("Firestore", "Native", "State/memory"),
    ("Cloud Storage", "Standard", "Documents"),
    ("Vertex AI", "Standard", "Model serving"),
    ("AlloyDB", "Standard", "pgvector embeddings"),
    ("Pub/Sub", "Standard", "Messaging"),
]

print(f"\n  {'Service':20s} {'Tier':>10} Purpose")
for svc, tier, purpose in services:
    print(f"  {svc:20s} {tier:>10} {purpose}")

print("\n  Deployment Steps:")
steps = [
    "1. gcloud builds submit --tag gcr.io/PROJECT/agent",
    "2. gcloud run deploy agent --image gcr.io/PROJECT/agent",
    "3. Configure Firestore + Vertex AI",
    "4. Set up Pub/Sub + monitoring",
]
for step in steps:
    print(f"    {step}")

print("\nDone!")
