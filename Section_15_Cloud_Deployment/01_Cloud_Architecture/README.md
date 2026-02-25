# Cloud Architecture for AI Agents

## Architecture Patterns

### Microservices Architecture
Decompose agent system into independent services:
- Agent Service (orchestration)
- LLM Gateway (model routing)
- RAG Service (retrieval)
- Tool Service (tool execution)
- Memory Service (state management)

### Event-Driven Architecture
Services communicate through events:
- Message queues (SQS, RabbitMQ, Kafka)
- Event bus (EventBridge, Pub/Sub)
- Async processing for long-running tasks

### API Gateway Pattern
```
Client -> API Gateway -> Load Balancer -> Agent Instances
                                              |
                              ┌────────────────┼────────────────┐
                              v                v                v
                         LLM Service    RAG Service     Tool Service
```

## Key Design Decisions
- **Managed vs Self-hosted LLMs**: API (OpenAI/Anthropic) vs self-hosted (vLLM, TGI)
- **Stateful vs Stateless**: Agent state in service vs external store
- **Sync vs Async**: Real-time vs background processing
- **Single-region vs Multi-region**: Latency vs complexity

## Infrastructure Requirements
- **Compute**: GPU for self-hosted models, CPU for orchestration
- **Storage**: Vector DB, graph DB, blob storage, cache
- **Networking**: Low-latency connections, VPN for security
- **Monitoring**: CloudWatch/Stackdriver + LLM observability

## For Architects
- Start with managed LLM APIs (OpenAI, Anthropic) for faster time-to-market
- Add self-hosted models later for cost optimization or data privacy
- Always design for horizontal scaling from day one