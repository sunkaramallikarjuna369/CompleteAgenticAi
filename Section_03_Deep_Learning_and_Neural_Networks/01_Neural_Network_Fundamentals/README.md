# Neural Network Fundamentals

## What is a Neural Network?

A neural network is a computational model inspired by the human brain. It consists of layers of interconnected nodes (neurons) that process information and learn to map inputs to outputs through training.

## Architecture

```
Input Layer → Hidden Layer(s) → Output Layer

  x1 ──┐
       ├──► [h1] ──┐
  x2 ──┤           ├──► [o1] → prediction
       ├──► [h2] ──┤
  x3 ──┘           ├──► [o2] → prediction
              [h3] ──┘
```

### Components

**Neuron (Node)**: The basic unit. Takes inputs, applies weights, adds bias, passes through activation function.
```
output = activation(w1*x1 + w2*x2 + ... + wn*xn + bias)
```

**Weights**: Learnable parameters that determine the strength of connections between neurons.

**Bias**: An additional learnable parameter that shifts the activation function.

**Layer Types:**
- **Input Layer**: Receives the raw data features
- **Hidden Layers**: Process and transform data (the "deep" in deep learning)
- **Output Layer**: Produces the final prediction

## Activation Functions

| Function | Formula | Range | Use Case |
|----------|---------|-------|----------|
| **ReLU** | max(0, x) | [0, infinity) | Most hidden layers (default choice) |
| **Sigmoid** | 1/(1+e^-x) | (0, 1) | Binary classification output |
| **Tanh** | (e^x - e^-x)/(e^x + e^-x) | (-1, 1) | Centered hidden layers |
| **Softmax** | e^xi / sum(e^xj) | (0, 1), sums to 1 | Multi-class classification output |
| **GELU** | x * Phi(x) | (-inf, inf) | Transformer models (GPT, BERT) |
| **Swish/SiLU** | x * sigmoid(x) | (-inf, inf) | Modern architectures |

## Backpropagation

The algorithm that trains neural networks:

1. **Forward Pass**: Input flows through the network to produce a prediction
2. **Loss Calculation**: Compare prediction to true label using loss function
3. **Backward Pass**: Calculate gradients of loss with respect to each weight (chain rule)
4. **Weight Update**: Adjust weights in the direction that reduces loss

```
Forward: Input → Layer 1 → Layer 2 → ... → Output → Loss
Backward: Loss → Gradients → Update weights layer by layer (chain rule)
```

## Key Concepts

### Epochs, Batches, and Iterations
- **Epoch**: One complete pass through the entire training dataset
- **Batch**: A subset of training data processed together
- **Batch Size**: Number of samples per batch (typically 32, 64, 128, 256)
- **Iteration**: One weight update (= one batch processed)

### Regularization Techniques
- **Dropout**: Randomly deactivate neurons during training (prevents co-adaptation)
- **Batch Normalization**: Normalize layer inputs for stable training
- **L1/L2 Regularization**: Penalize large weights
- **Early Stopping**: Stop training when validation loss stops improving

### Learning Rate
- Too high: Training diverges (loss oscillates or increases)
- Too low: Training is extremely slow
- Learning rate scheduling: Start high, reduce over time
- Adam optimizer: Adapts learning rate per parameter

## Deep Networks: Why "Deep" Matters

Each layer learns increasingly abstract features:
```
Layer 1: Edges, textures (low-level features)
Layer 2: Shapes, patterns (mid-level features)
Layer 3: Object parts (high-level features)
Layer 4+: Complete objects, concepts (abstract features)
```

This hierarchical feature learning is what makes deep networks powerful — and it's the same principle behind how LLMs learn increasingly complex language patterns.

## Connection to Agentic AI

- LLMs are massive neural networks with billions of parameters
- Understanding backpropagation helps you understand fine-tuning
- Dropout and regularization concepts apply to agent reliability
- The forward pass of a neural network IS the inference that happens every time an agent thinks
