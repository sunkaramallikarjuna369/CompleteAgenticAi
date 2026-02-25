"""
Graph Neural Networks
=====================
Section 13

Demonstrates GNN concepts: node features,
message passing, and graph classification.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("GRAPH NEURAL NETWORKS")
print("=" * 60)

# 1. Graph Representation
print("\n1. GRAPH WITH NODE FEATURES")
print("-" * 40)

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    def add_node(self, nid, features):
        self.nodes[nid] = features
    def add_edge(self, src, dst):
        self.edges.append((src, dst))
        self.edges.append((dst, src))
    def neighbors(self, nid):
        return [dst for src, dst in self.edges if src == nid]

random.seed(42)
g = Graph()
for i in range(5):
    g.add_node(i, [random.gauss(0, 1) for _ in range(3)])
g.add_edge(0, 1); g.add_edge(1, 2); g.add_edge(2, 3); g.add_edge(3, 4); g.add_edge(0, 4)

print("  Nodes and features:")
for nid, feat in g.nodes.items():
    print(f"    Node {nid}: [{', '.join(f'{f:.2f}' for f in feat)}]")

# 2. Message Passing
print("\n2. MESSAGE PASSING (1 layer)")
print("-" * 40)

def message_passing(graph, weights=None):
    new_features = {}
    dim = len(list(graph.nodes.values())[0])
    if weights is None:
        weights = [[random.gauss(0, 0.5) for _ in range(dim)] for _ in range(dim)]

    for nid in graph.nodes:
        nbrs = graph.neighbors(nid)
        if not nbrs:
            new_features[nid] = graph.nodes[nid]
            continue
        # Aggregate neighbor features (mean)
        agg = [0.0] * dim
        for nbr in nbrs:
            for d in range(dim):
                agg[d] += graph.nodes[nbr][d]
        agg = [a / len(nbrs) for a in agg]
        # Combine with self features
        combined = [(graph.nodes[nid][d] + agg[d]) / 2 for d in range(dim)]
        # Apply weights + ReLU
        new_feat = [max(0, sum(weights[i][j] * combined[j] for j in range(dim))) for i in range(dim)]
        new_features[nid] = new_feat
    return new_features

updated = message_passing(g)
print("  After message passing:")
for nid, feat in updated.items():
    print(f"    Node {nid}: [{', '.join(f'{f:.2f}' for f in feat)}]")

# 3. Graph-Level Readout
print("\n3. GRAPH CLASSIFICATION (Readout)")
print("-" * 40)

def graph_readout(features):
    dim = len(list(features.values())[0])
    pooled = [0.0] * dim
    for feat in features.values():
        for d in range(dim):
            pooled[d] += feat[d]
    pooled = [p / len(features) for p in pooled]
    # Simple classifier
    score = sum(pooled) / len(pooled)
    label = "Class A" if score > 0 else "Class B"
    return pooled, label

pooled, label = graph_readout(updated)
print(f"  Pooled features: [{', '.join(f'{f:.2f}' for f in pooled)}]")
print(f"  Classification: {label}")

print("\nDone!")
