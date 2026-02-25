# Agent Memory Systems

## Types of Memory
### Working Memory (Short-term)
The current conversation context. Limited by context window.

### Long-term Memory
Persistent storage across conversations. Vector databases, key-value stores.

### Episodic Memory
Memory of past experiences and interactions. Helps agents learn from history.

### Semantic Memory
Factual knowledge and concepts. RAG knowledge bases.

### Procedural Memory
How to do things. Stored as tools, workflows, and learned procedures.

## Memory Architecture
```
User Input -> Working Memory (context window)
                  |
                  v
          Memory Manager
         /      |       \
   Episodic  Semantic  Procedural
   (past     (facts,   (tools,
   events)   knowledge) workflows)
```

## For Agentic AI
- Memory is what makes agents persistent and personalized
- Combining memory types creates more capable agents