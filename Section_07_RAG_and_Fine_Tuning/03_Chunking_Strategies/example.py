"""
Chunking Strategies
===================
Section 07

Demonstrates text chunking: fixed-size, sentence-based,
and recursive chunking.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("CHUNKING STRATEGIES")
print("=" * 60)

text = """Artificial intelligence is transforming how we build software. Machine learning models can now understand and generate human language. Large language models like GPT have revolutionized NLP. RAG systems combine retrieval with generation. Vector databases enable efficient similarity search. Chunking is essential for processing long documents. Different strategies work best for different use cases. Fixed-size chunks are simple but may break context. Sentence-based chunks preserve semantic boundaries. Recursive chunking adapts to document structure."""

# 1. Fixed-size chunking
print("\n1. FIXED-SIZE CHUNKING")
print("-" * 40)

def fixed_chunk(text, size=100, overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append(text[start:end])
        start += size - overlap
    return chunks

chunks = fixed_chunk(text, size=80, overlap=10)
for i, chunk in enumerate(chunks):
    print(f"  Chunk {i} ({len(chunk)} chars): {chunk[:50]}...")

# 2. Sentence-based chunking
print("\n2. SENTENCE-BASED CHUNKING")
print("-" * 40)

def sentence_chunk(text, max_sentences=2):
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    for i in range(0, len(sentences), max_sentences):
        chunk = ' '.join(sentences[i:i+max_sentences])
        chunks.append(chunk)
    return chunks

chunks = sentence_chunk(text, max_sentences=2)
for i, chunk in enumerate(chunks):
    print(f"  Chunk {i}: {chunk[:60]}...")

# 3. Comparison
print("\n3. STRATEGY COMPARISON")
print("-" * 40)

strategies = {
    "Fixed (80 chars)": fixed_chunk(text, 80, 10),
    "Fixed (150 chars)": fixed_chunk(text, 150, 20),
    "Sentence (2 per)": sentence_chunk(text, 2),
    "Sentence (3 per)": sentence_chunk(text, 3),
}

print(f"  {'Strategy':20s} {'Chunks':>7} {'Avg Size':>9} {'Min':>5} {'Max':>5}")
for name, chunks in strategies.items():
    sizes = [len(c) for c in chunks]
    avg = sum(sizes)/len(sizes)
    print(f"  {name:20s} {len(chunks):>7} {avg:>9.0f} {min(sizes):>5} {max(sizes):>5}")

print("\nDone!")
