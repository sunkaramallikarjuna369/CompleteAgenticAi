"""
Knowledge Graphs
================
Section 13

Demonstrates knowledge graphs: entities, relationships,
traversal, and querying.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("KNOWLEDGE GRAPHS")
print("=" * 60)

class KnowledgeGraph:
    def __init__(self):
        self.entities = {}
        self.relations = []
    def add_entity(self, name, etype, props=None):
        self.entities[name] = {"type": etype, "props": props or {}}
    def add_relation(self, src, rel, tgt):
        self.relations.append((src, rel, tgt))
    def query(self, entity):
        outgoing = [(r, t) for s, r, t in self.relations if s == entity]
        incoming = [(s, r) for s, r, t in self.relations if t == entity]
        return outgoing, incoming
    def path(self, start, end, visited=None):
        if visited is None: visited = set()
        if start == end: return [start]
        visited.add(start)
        for _, _, tgt in self.relations:
            if tgt not in visited:
                for s, _, t in self.relations:
                    if s == start and t == tgt:
                        p = self.path(tgt, end, visited)
                        if p: return [start] + p
        return None

kg = KnowledgeGraph()
kg.add_entity("Python", "Language", {"year": 1991})
kg.add_entity("TensorFlow", "Framework", {"creator": "Google"})
kg.add_entity("PyTorch", "Framework", {"creator": "Meta"})
kg.add_entity("LangChain", "Framework", {"purpose": "LLM apps"})
kg.add_entity("Google", "Company")
kg.add_entity("Meta", "Company")

kg.add_relation("TensorFlow", "built_with", "Python")
kg.add_relation("PyTorch", "built_with", "Python")
kg.add_relation("LangChain", "built_with", "Python")
kg.add_relation("Google", "created", "TensorFlow")
kg.add_relation("Meta", "created", "PyTorch")

print(f"  Entities: {len(kg.entities)}, Relations: {len(kg.relations)}")

out, inc = kg.query("Python")
print(f"\n  Query 'Python':")
print(f"    Outgoing: {out}")
print(f"    Incoming: {[(s, r) for s, r in inc]}")

path = kg.path("Google", "Python")
print(f"\n  Path Google->Python: {' -> '.join(path) if path else 'None'}")

print("\nDone!")
