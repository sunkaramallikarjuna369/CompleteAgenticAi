# Recurrent Neural Networks (RNNs) & LSTMs

## Overview
RNNs process sequential data (text, time series, audio) by maintaining a hidden state that serves as memory. Unlike feedforward networks, RNNs loop information back, enabling them to handle variable-length sequences.

## RNN Architecture
```
h_t = activation(W_h * h_{t-1} + W_x * x_t + b)
y_t = W_y * h_t + b_y

Unrolled: x1 -> [RNN] -> h1 -> [RNN] -> h2 -> [RNN] -> h3
```

## The Vanishing Gradient Problem
Gradients shrink exponentially during backpropagation through time, preventing learning of long-range dependencies.

## LSTM (Long Short-Term Memory)
LSTMs solve vanishing gradients with gates:
- **Forget Gate**: What to discard from cell state
- **Input Gate**: What new information to store
- **Output Gate**: What to output from cell state
- **Cell State**: Long-term memory highway

## GRU (Gated Recurrent Unit)
Simplified LSTM with 2 gates (reset, update). Fewer parameters, comparable performance.

## Bidirectional RNNs
Process sequences forward AND backward for richer context.

## Why Transformers Replaced RNNs
| Property | RNN/LSTM | Transformer |
|----------|----------|-------------|
| Processing | Sequential | Parallel |
| Long-range deps | Difficult | Direct attention |
| Training speed | Slow | Fast |
| Scalability | Limited | Billions of params |

## Connection to Agentic AI
- LSTM gating inspired agent memory management
- RNN "memory" concept parallels agent working memory
- Understanding RNNs shows WHY Transformers won
