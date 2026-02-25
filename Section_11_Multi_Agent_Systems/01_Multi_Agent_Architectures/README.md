# Multi-Agent Architectures

## Why Multi-Agent?
- Complex tasks need specialized expertise
- Parallel processing for speed
- Separation of concerns
- Scalability through composition

## Architecture Patterns
### Supervisor
One agent manages and delegates to worker agents.

### Swarm
Decentralized agents self-organize. OpenAI Swarm pattern.

### Hierarchical
Multiple levels of management. Managers delegate to sub-managers.

### Mesh
All agents can communicate with all others. Flexible but complex.

### Pipeline
Agents process sequentially, each adding value.

## For Architects
- Supervisor is the most common production pattern
- Start with 2-3 agents, scale as needed