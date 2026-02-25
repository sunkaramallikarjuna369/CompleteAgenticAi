# Vector Databases

## What Are Vector Databases?
Databases optimized for storing and searching high-dimensional vectors (embeddings).

## Key Vector Databases
| Database | Type | Key Feature |
|----------|------|-------------|
| Pinecone | Managed | Fully managed, easy to use |
| Weaviate | Open-source | Hybrid search, GraphQL |
| Qdrant | Open-source | Rust-based, fast |
| Chroma | Open-source | Simple, Python-native |
| Milvus | Open-source | Scalable, GPU support |
| pgvector | Extension | PostgreSQL extension |

## Similarity Search
- Cosine Similarity: Angle between vectors
- Euclidean Distance: Straight-line distance
- Dot Product: Magnitude-aware similarity

## Embedding Models
- OpenAI text-embedding-ada-002 / text-embedding-3-small
- Cohere embed-v3
- all-MiniLM-L6-v2 (open-source)
- BGE, E5 (open-source)

## For Agentic AI
- Vector DBs are the memory backbone of RAG agents
- Choice of embedding model affects retrieval quality