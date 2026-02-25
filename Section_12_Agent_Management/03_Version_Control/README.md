# Agent Version Control

## What to Version
- System prompts
- Tool definitions
- Model configurations (temperature, model name)
- RAG configurations (chunk size, top-k)
- Guardrail rules

## A/B Testing
Run two agent versions simultaneously, compare metrics:
- Task completion rate
- User satisfaction
- Cost per interaction
- Latency

## Tools
- Git for prompt/config versioning
- LangSmith for evaluation
- Feature flags for gradual rollout

## For Agentic AI
- Version everything, test everything
- Gradual rollout prevents production incidents