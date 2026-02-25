"""
Multimodal Models
=================
Section 05

Demonstrates multimodal concepts: cross-modal embeddings,
text-image similarity, and fusion strategies.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import math, random

print("=" * 60)
print("MULTIMODAL AI")
print("=" * 60)

print("\n1. CROSS-MODAL EMBEDDINGS")
print("-" * 40)

class MultimodalEmbedder:
    def __init__(self, dim=4):
        random.seed(42)
        self.dim = dim
        self.text_proj = [[random.gauss(0, 0.5) for _ in range(dim)] for _ in range(dim)]
        self.image_proj = [[random.gauss(0, 0.5) for _ in range(dim)] for _ in range(dim)]

    def embed_text(self, text_features):
        return [sum(self.text_proj[i][j]*text_features[j] for j in range(self.dim)) for i in range(self.dim)]

    def embed_image(self, image_features):
        return [sum(self.image_proj[i][j]*image_features[j] for j in range(self.dim)) for i in range(self.dim)]

    def similarity(self, a, b):
        dot = sum(x*y for x,y in zip(a,b))
        na = math.sqrt(sum(x**2 for x in a))
        nb = math.sqrt(sum(x**2 for x in b))
        return dot/(na*nb) if na and nb else 0

embedder = MultimodalEmbedder(4)

texts = {
    "cat photo": [0.9, 0.1, 0.3, 0.2],
    "dog photo": [0.8, 0.2, 0.4, 0.1],
    "car image": [0.1, 0.8, 0.1, 0.7],
}
images = {
    "cat.jpg": [0.85, 0.15, 0.35, 0.25],
    "dog.jpg": [0.75, 0.25, 0.45, 0.15],
    "car.jpg": [0.15, 0.75, 0.15, 0.65],
}

print("  Text-Image Similarity:")
for tname, tfeat in texts.items():
    te = embedder.embed_text(tfeat)
    for iname, ifeat in images.items():
        ie = embedder.embed_image(ifeat)
        sim = embedder.similarity(te, ie)
        print(f"    '{tname}' vs '{iname}': {sim:.3f}")

# Fusion strategies
print("\n2. FUSION STRATEGIES")
print("-" * 40)

strategies = [
    ("Early Fusion", "Concatenate raw features before model"),
    ("Late Fusion", "Process separately, combine predictions"),
    ("Cross-Attention", "Attend across modalities in transformer"),
]
for name, desc in strategies:
    print(f"  {name:18s}: {desc}")

print("\nDone!")
