# Chunking Strategies

## Why Chunking Matters
Documents must be split into chunks for embedding and retrieval. Chunk size and strategy dramatically affect RAG quality.

## Strategies
- **Fixed Size**: Split every N characters/tokens with overlap
- **Recursive**: Split by paragraphs, then sentences, then characters
- **Semantic**: Split at topic boundaries using embeddings
- **Document-Aware**: Respect headers, sections, tables
- **Sentence-Level**: Split at sentence boundaries

## Key Parameters
| Parameter | Typical Range | Effect |
|-----------|--------------|--------|
| Chunk size | 256-1024 tokens | Larger = more context, less precise |
| Overlap | 10-20% of chunk | Prevents losing context at boundaries |
| Top-K | 3-10 chunks | More = more context, higher cost |

## For Agentic AI
- Chunking strategy directly affects agent answer quality
- Too small = missing context, too large = noise