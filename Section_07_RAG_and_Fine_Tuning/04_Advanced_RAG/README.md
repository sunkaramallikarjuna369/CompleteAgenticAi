# Advanced RAG

## Hybrid Search
Combine vector (semantic) search with keyword (BM25) search for better results.

## Reranking
Use a cross-encoder to rerank retrieved documents by relevance.
- Cohere Rerank, BGE Reranker, ColBERT

## Query Transformation
- **Query Expansion**: Generate multiple query variations
- **HyDE**: Generate hypothetical answer, use it for retrieval
- **Step-back Prompting**: Ask a more general question first

## Multi-Index RAG
Search across multiple knowledge bases and combine results.

## Agentic RAG
The agent decides WHEN and HOW to retrieve:
- Which knowledge base to search
- Whether to refine the query
- When to stop retrieving

## For Agentic AI
- Agentic RAG gives agents intelligent retrieval control
- Hybrid search + reranking is the production standard