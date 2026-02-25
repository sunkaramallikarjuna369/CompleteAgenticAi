# Convolutional Neural Networks (CNNs)

## Overview

CNNs are specialized neural networks designed for processing grid-like data, particularly images. They use convolutional filters to automatically learn spatial features at multiple levels of abstraction.

## How CNNs Work

### Convolution Operation
A small filter (kernel) slides across the input, computing dot products at each position to produce a feature map.

```
Input Image (5x5)     Filter (3x3)      Feature Map (3x3)
┌─────────────┐      ┌─────────┐       ┌───────────┐
│ 1 0 1 0 1   │      │ 1 0 1   │       │ 4 3 4     │
│ 0 1 0 1 0   │  *   │ 0 1 0   │   =   │ 2 4 3     │
│ 1 0 1 0 1   │      │ 1 0 1   │       │ 4 3 4     │
│ 0 1 0 1 0   │      └─────────┘       └───────────┘
│ 1 0 1 0 1   │
└─────────────┘
```

### Key Components

**Convolutional Layer**: Applies multiple learned filters to detect features (edges, textures, shapes)
**Pooling Layer**: Reduces spatial dimensions (Max Pooling takes the maximum value in each region)
**Flatten**: Converts 2D feature maps to 1D vector for classification
**Fully Connected Layer**: Standard neural network layers for final classification

### CNN Architecture Pattern
```
Input → [Conv → ReLU → Pool] × N → Flatten → FC → FC → Output
```

## Feature Hierarchy

```
Layer 1: Edges and gradients
Layer 2: Textures and patterns
Layer 3: Object parts (eyes, wheels)
Layer 4: Complete objects (faces, cars)
Layer 5+: Scenes and concepts
```

## Key Architectures

| Model | Year | Layers | Key Innovation | Error Rate (ImageNet) |
|-------|------|--------|---------------|----------------------|
| **LeNet** | 1998 | 5 | First practical CNN | N/A |
| **AlexNet** | 2012 | 8 | GPU training, ReLU, Dropout | 16.4% |
| **VGG** | 2014 | 16-19 | Small 3x3 filters everywhere | 7.3% |
| **GoogLeNet** | 2014 | 22 | Inception modules (parallel paths) | 6.7% |
| **ResNet** | 2015 | 50-152 | Skip connections (residual learning) | 3.6% |
| **DenseNet** | 2017 | 121+ | Dense connections between all layers | 3.4% |
| **EfficientNet** | 2019 | Variable | Compound scaling of width/depth/resolution | 2.9% |

## ResNet: The Most Important CNN Innovation

Skip connections (residual connections) allow gradients to flow directly through the network, enabling training of very deep networks (100+ layers):

```
Input → Conv → ReLU → Conv → (+) → ReLU → Output
  |                              ↑
  └──────── Skip Connection ─────┘
```

This same idea powers Transformers — residual connections are used throughout GPT and BERT architectures.

## Connection to Agentic AI

- Vision Transformers evolved FROM CNNs — understanding CNNs helps you understand modern vision models
- ResNet's skip connections are the precursor to Transformer residual connections
- Multimodal agents (GPT-4V, Gemini) use CNN-inspired vision encoders
- Feature extraction concepts from CNNs apply to how agents process visual inputs
