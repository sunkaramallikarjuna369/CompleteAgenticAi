"""
Graph Databases
===============
Section 13

Demonstrates graph database concepts: nodes, edges,
Cypher-like queries, and traversal.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("GRAPH DATABASES")
print("=" * 60)

class GraphDB:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    def create_node(self, nid, label, props):
        self.nodes[nid] = {"label": label, "props": props}
    def create_edge(self, from_id, to_id, rel_type):
        self.edges.append({"from": from_id, "to": to_id, "type": rel_type})
    def match(self, label=None, **props):
        results = []
        for nid, node in self.nodes.items():
            if label and node["label"] != label: continue
            if all(node["props"].get(k) == v for k, v in props.items()):
                results.append((nid, node))
        return results
    def neighbors(self, nid, depth=1):
        if depth == 0: return {nid}
        result = {nid}
        for e in self.edges:
            if e["from"] == nid: result |= self.neighbors(e["to"], depth-1)
            if e["to"] == nid: result |= self.neighbors(e["from"], depth-1)
        return result

db = GraphDB()
db.create_node("alice", "Person", {"name": "Alice", "role": "Engineer"})
db.create_node("bob", "Person", {"name": "Bob", "role": "Researcher"})
db.create_node("proj1", "Project", {"name": "AI Agent"})
db.create_node("py", "Tech", {"name": "Python"})

db.create_edge("alice", "proj1", "WORKS_ON")
db.create_edge("bob", "proj1", "WORKS_ON")
db.create_edge("alice", "bob", "COLLABORATES")
db.create_edge("proj1", "py", "USES")

print(f"  Nodes: {len(db.nodes)}, Edges: {len(db.edges)}")

print("\n  MATCH (p:Person):")
for nid, node in db.match("Person"):
    print(f"    {nid}: {node['props']}")

print(f"\n  Neighbors of 'alice' (depth=2):")
for nid in db.neighbors("alice", 2):
    print(f"    {nid}: {db.nodes[nid]['label']}")

print("\nDone!")
