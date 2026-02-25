# Large Language Models

## What Are LLMs?
Large neural networks (billions of parameters) trained on massive text corpora to predict next tokens. They learn language understanding, reasoning, and knowledge.

## Key LLMs
| Model | Provider | Parameters | Context | Open? |
|-------|----------|-----------|---------|-------|
| GPT-4 | OpenAI | ~1.8T | 128K | No |
| Claude 3.5 | Anthropic | Undisclosed | 200K | No |
| Gemini | Google | Undisclosed | 1M+ | Partial |
| Llama 3 | Meta | 8B-405B | 128K | Yes |
| Mistral | Mistral AI | 7B-8x22B | 32K | Yes |

## How LLMs Work
1. Tokenization: Text -> tokens
2. Embedding: Tokens -> vectors
3. Transformer layers: Self-attention + FFN
4. Output: Probability distribution over next token
5. Autoregressive: Generate one token at a time

## Pre-training vs Fine-tuning
- Pre-training: Learn language from massive corpora (expensive)
- Fine-tuning: Adapt to specific tasks (cheaper)
- RLHF: Align with human preferences

## For Agentic AI
LLMs ARE the brain of every AI agent. Understanding their capabilities and limitations is essential.