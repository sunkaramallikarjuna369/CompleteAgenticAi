# Cost Management

## Cost Drivers
- Input tokens (prompt + context)
- Output tokens (response)
- Number of LLM calls per task
- Model choice (GPT-4 vs GPT-3.5 vs open-source)

## Optimization Strategies
- **Prompt Optimization**: Shorter prompts, fewer examples
- **Caching**: Cache common queries and responses
- **Model Routing**: Use cheaper models for simple tasks
- **Token Budgets**: Set limits per task/user
- **Batching**: Combine multiple requests
- **Open-Source Models**: Self-host for high-volume tasks

## Cost Comparison
| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| GPT-4 | $30 | $60 |
| GPT-4o | $5 | $15 |
| GPT-3.5 | $0.50 | $1.50 |
| Claude 3.5 Sonnet | $3 | $15 |
| Llama 3 (self-hosted) | ~$0.20 | ~$0.20 |

## For Architects
- Cost management is critical for enterprise adoption
- Model routing can reduce costs 5-10x