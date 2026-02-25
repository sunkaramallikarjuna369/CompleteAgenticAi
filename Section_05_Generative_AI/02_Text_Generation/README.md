# Text Generation

## Autoregressive Generation
Generate one token at a time, feeding output back as input.

## Decoding Strategies
- **Greedy**: Always pick highest probability token
- **Beam Search**: Track top-k sequences
- **Temperature**: Control randomness (0=deterministic, 1=creative)
- **Top-k Sampling**: Sample from top k tokens
- **Top-p (Nucleus)**: Sample from smallest set with cumulative prob >= p

## Key Parameters
| Parameter | Effect | Typical Value |
|-----------|--------|---------------|
| Temperature | Randomness | 0.0-1.0 |
| Top-p | Diversity | 0.9-0.95 |
| Max tokens | Length limit | Task-dependent |
| Stop sequences | End generation | Task-dependent |

## For Agentic AI
- Agents need low temperature for reliable tool calls
- Higher temperature for creative tasks
- Stop sequences prevent runaway generation