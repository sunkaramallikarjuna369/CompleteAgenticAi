# Attention Mechanisms

## Overview
Attention allows neural networks to focus on relevant parts of input. It is THE core innovation behind Transformers and all modern LLMs.

## Types of Attention
1. **Self-Attention**: Each token attends to all others in same sequence
2. **Cross-Attention**: Tokens from one sequence attend to another
3. **Causal (Masked)**: Only attend to previous positions (GPT, Claude)
4. **Multi-Head**: Multiple parallel attention operations

## Scaled Dot-Product Attention
```
Attention(Q, K, V) = softmax(Q * K^T / sqrt(d_k)) * V
```

## Attention Optimizations
| Optimization | How | Impact |
|-------------|-----|--------|
| Flash Attention | Tiled computation | 2-4x faster, less memory |
| KV Cache | Store previous K,V | Avoid recomputation |
| Multi-Query (MQA) | Share K,V across heads | Smaller cache |
| Grouped-Query (GQA) | Groups share K,V | Balance quality/speed |
| Sparse Attention | Attend to subset only | Linear scaling |

## Connection to Agentic AI
- Attention IS how agents "think" about context
- Context window limits = attention computation limits
- KV cache optimization affects agent response speed
- Prompt design should consider attention patterns
