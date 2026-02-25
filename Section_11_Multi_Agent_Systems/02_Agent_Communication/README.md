# Agent Communication

## Communication Patterns
### Message Passing
Agents send structured messages to each other.

### Shared State
Agents read/write to a shared state store.

### Event-Driven
Agents publish/subscribe to events.

### Direct Function Calls
Agents invoke each other's capabilities directly.

## Message Format
```json
{"from": "researcher", "to": "writer", "type": "task_result", "content": {...}}
```

## For Agentic AI
- Clear communication protocols prevent agent confusion
- Structured messages enable reliable multi-agent workflows