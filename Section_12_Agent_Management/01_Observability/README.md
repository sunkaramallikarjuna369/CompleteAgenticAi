# Agent Observability

## Why Observability?
Agents are non-deterministic. You MUST log every step to debug issues and improve performance.

## What to Log
- Every LLM call (input, output, tokens, latency, cost)
- Tool calls (name, arguments, results, errors)
- Agent decisions (which tool, why)
- Memory operations (read, write)
- User interactions

## Tools
- **LangSmith**: LangChain's observability platform
- **Langfuse**: Open-source LLM observability
- **Helicone**: LLM proxy with logging
- **Portkey**: AI gateway with observability
- **OpenTelemetry**: Standard observability framework

## For Agentic AI
- Observability is NON-NEGOTIABLE for production agents
- Without it, debugging is nearly impossible