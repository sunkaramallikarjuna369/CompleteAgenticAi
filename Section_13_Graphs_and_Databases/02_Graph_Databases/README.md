# Graph Databases

## What Are Graph Databases?
Databases optimized for storing and querying graph-structured data (nodes and edges).

## Key Graph Databases
| Database | Type | Query Language | Best For |
|----------|------|---------------|----------|
| Neo4j | Native graph | Cypher | General purpose, most popular |
| Amazon Neptune | Managed | Gremlin/SPARQL | AWS ecosystem |
| ArangoDB | Multi-model | AQL | Graph + document + key-value |
| TigerGraph | Native graph | GSQL | Enterprise analytics |
| Memgraph | In-memory | Cypher | Real-time graph analytics |

## Cypher Query Language (Neo4j)
```cypher
// Find all friends of Alice
MATCH (a:Person {name: 'Alice'})-[:FRIENDS_WITH]->(friend)
RETURN friend.name

// Find shortest path
MATCH path = shortestPath((a:Person)-[*]-(b:Person))
WHERE a.name = 'Alice' AND b.name = 'Bob'
RETURN path
```

## Graph vs Relational
| Feature | Relational (SQL) | Graph (Neo4j) |
|---------|-----------------|---------------|
| Relationships | JOINs (slow for deep) | Native traversal (fast) |
| Schema | Fixed | Flexible |
| Multi-hop queries | Complex JOINs | Simple pattern matching |
| Best for | Structured data | Connected data |

## For Agentic AI
- Graph databases power knowledge graph-based agents
- Multi-hop reasoning requires efficient graph traversal
- Neo4j is the most common choice for agent knowledge bases