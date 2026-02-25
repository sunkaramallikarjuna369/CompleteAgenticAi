"""
Haystack Framework
==================
Section 09

Demonstrates Haystack concepts: pipelines, components,
and document processing.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("HAYSTACK FRAMEWORK CONCEPTS")
print("=" * 60)

class Component:
    def __init__(self, name):
        self.name = name
    def run(self, data):
        raise NotImplementedError

class DocumentCleaner(Component):
    def __init__(self):
        super().__init__("DocumentCleaner")
    def run(self, data):
        cleaned = [d.strip().lower() for d in data["documents"]]
        return {"documents": cleaned}

class DocumentSplitter(Component):
    def __init__(self, split_length=5):
        super().__init__("DocumentSplitter")
        self.split_length = split_length
    def run(self, data):
        chunks = []
        for doc in data["documents"]:
            words = doc.split()
            for i in range(0, len(words), self.split_length):
                chunks.append(" ".join(words[i:i+self.split_length]))
        return {"documents": chunks}

class Retriever(Component):
    def __init__(self):
        super().__init__("Retriever")
    def run(self, data):
        query = data.get("query", "").lower()
        q_words = set(query.split())
        scored = []
        for doc in data["documents"]:
            d_words = set(doc.split())
            score = len(q_words & d_words)
            scored.append((score, doc))
        scored.sort(key=lambda x: -x[0])
        return {"documents": [d for _, d in scored[:3]], "query": query}

class HaystackPipeline:
    def __init__(self):
        self.components = []
    def add(self, component):
        self.components.append(component)
        return self
    def run(self, data):
        for comp in self.components:
            data = comp.run(data)
            print(f"  [{comp.name:20s}] -> {len(data.get('documents', []))} items")
        return data

# Build pipeline
pipeline = HaystackPipeline()
pipeline.add(DocumentCleaner())
pipeline.add(DocumentSplitter(split_length=6))
pipeline.add(Retriever())

docs = [
    "  AI Agents Use Tools and Memory for Autonomous Task Execution  ",
    "  RAG Systems Retrieve Documents to Augment Language Model Responses  ",
    "  Haystack Provides Building Blocks for NLP Pipelines and Search  ",
]

print("  Running pipeline:")
result = pipeline.run({"documents": docs, "query": "AI agents tools"})
print(f"\n  Top results:")
for doc in result["documents"]:
    print(f"    - {doc}")

print("\nDone!")
