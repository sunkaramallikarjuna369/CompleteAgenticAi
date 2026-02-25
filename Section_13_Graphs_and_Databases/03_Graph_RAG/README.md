# GraphRAG

## What is GraphRAG?
Combining knowledge graphs with vector-based RAG to get the best of both: semantic search + structured reasoning.

## Why GraphRAG?
- **Vector RAG limitations**: Can't answer multi-hop questions well
- **Graph advantages**: Explicit relationships enable reasoning across entities
- **Combined**: Semantic search finds relevant context, graph traversal finds connections

## Architecture
```
Query -> [Vector Search] -> Relevant chunks
      -> [Graph Traversal] -> Related entities & relationships
      -> Combine context -> LLM -> Answer
```

## Microsoft GraphRAG
Microsoft's approach:
1. Build a knowledge graph from documents
2. Create community summaries (hierarchical)
3. Use graph structure for global queries
4. Combine with local vector search

## Implementation Options
- Neo4j + LangChain GraphRAG
- Microsoft GraphRAG library
- LlamaIndex Knowledge Graph Index
- Custom graph + vector hybrid

## For Agentic AI
- GraphRAG is the next evolution of agent knowledge
- Especially powerful for enterprise agents with complex domain knowledge
- Enables agents to answer "why" and "how" questions, not just "what"