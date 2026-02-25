# Knowledge Graphs

## What is a Knowledge Graph?
A structured representation of knowledge as entities (nodes) and relationships (edges). Example: (Albert Einstein) --[born_in]--> (Germany)

## Components
- **Entities**: People, places, concepts, objects
- **Relationships**: Connections between entities (typed, directed)
- **Properties**: Attributes of entities and relationships
- **Ontology**: Schema defining types and valid relationships

## Building Knowledge Graphs
1. **Entity Extraction**: Use NER to identify entities in text
2. **Relation Extraction**: Identify relationships between entities
3. **Entity Resolution**: Merge duplicate entities
4. **Knowledge Fusion**: Combine information from multiple sources
5. **Validation**: Ensure consistency and accuracy

## Notable Knowledge Graphs
- Google Knowledge Graph (500B+ facts)
- Wikidata (100M+ items)
- DBpedia (extracted from Wikipedia)
- YAGO (academic knowledge graph)

## For Agentic AI
- Knowledge graphs provide structured reasoning capabilities
- Agents can traverse graphs to find connections and answer complex queries
- Graph + RAG (GraphRAG) dramatically improves retrieval quality for complex questions