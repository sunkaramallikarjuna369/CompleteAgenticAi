"""
Azure Deployment
================
Section 15

Demonstrates Azure deployment patterns for AI agents.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("AZURE DEPLOYMENT FOR AI AGENTS")
print("=" * 60)

services = [
    ("Azure Functions", "Consumption", "Agent logic"),
    ("Container Apps", "Standard", "Long-running agents"),
    ("Cosmos DB", "Serverless", "State/memory"),
    ("Blob Storage", "Hot", "Documents"),
    ("AI Search", "Standard", "Vector search"),
    ("OpenAI Service", "Standard", "LLM inference"),
    ("Monitor", "Standard", "Observability"),
]

print(f"\n  {'Service':25s} {'SKU':>12} Purpose")
for svc, sku, purpose in services:
    print(f"  {svc:25s} {sku:>12} {purpose}")

rates = {"Azure Functions": 15, "Container Apps": 50, "Cosmos DB": 25,
         "Blob Storage": 5, "AI Search": 250, "OpenAI Service": 200, "Monitor": 10}
total = sum(rates.values())
print(f"\n  Estimated monthly cost: ${total}")

print("\nDone!")
