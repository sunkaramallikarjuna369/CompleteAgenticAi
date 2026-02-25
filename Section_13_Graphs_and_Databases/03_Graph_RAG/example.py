"""
Graph RAG
=========
Section 13

Demonstrates Graph RAG: combining knowledge graphs
with retrieval-augmented generation.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("GRAPH RAG")
print("=" * 60)

class GraphRAG:
    def __init__(self):
        self.entities = {}
        self.relations = []
        self.documents = {}
    def add_entity(self, name, etype, desc):
        self.entities[name] = {"type": etype, "desc": desc}
    def add_relation(self, src, rel, tgt):
        self.relations.append((src, rel, tgt))
    def add_document(self, doc_id, text, linked):
        self.documents[doc_id] = {"text": text, "entities": linked}
    def graph_context(self, entity):
        ctx = []
        if entity in self.entities:
            ctx.append(f"{entity}: {self.entities[entity]['desc']}")
        for s, r, t in self.relations:
            if s == entity or t == entity:
                ctx.append(f"{s} --{r}--> {t}")
        return ctx
    def retrieve(self, query, top_k=2):
        q_words = set(query.lower().split())
        scored = []
        for did, doc in self.documents.items():
            d_words = set(doc["text"].lower().split())
            score = len(q_words & d_words)
            graph_ctx = []
            for ent in doc["entities"]:
                graph_ctx.extend(self.graph_context(ent))
            scored.append((score, did, doc["text"], graph_ctx))
        scored.sort(key=lambda x: -x[0])
        return scored[:top_k]

grag = GraphRAG()
grag.add_entity("LangChain", "Framework", "Framework for LLM apps")
grag.add_entity("RAG", "Technique", "Retrieval-Augmented Generation")
grag.add_entity("VectorDB", "Technology", "Stores embeddings")
grag.add_relation("LangChain", "supports", "RAG")
grag.add_relation("RAG", "uses", "VectorDB")

grag.add_document("d1", "LangChain provides tools for building RAG applications", ["LangChain", "RAG"])
grag.add_document("d2", "RAG retrieves documents to augment generation", ["RAG"])

query = "How does LangChain support RAG?"
results = grag.retrieve(query)

print(f"  Query: {query}")
for score, did, text, ctx in results:
    print(f"\n  [{did}] score={score}")
    print(f"  Text: {text[:60]}")
    print(f"  Graph context ({len(ctx)} facts):")
    for c in ctx[:3]:
        print(f"    - {c}")

print("\nDone!")
