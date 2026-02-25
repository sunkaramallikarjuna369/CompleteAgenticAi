# Transfer Learning

## Overview

Transfer Learning is the technique of taking a model trained on one task and adapting it for a different but related task. It is the single most important technique in modern AI — it's why we can build powerful AI agents without training from scratch.

## Why Transfer Learning Matters

**Without Transfer Learning:**
- Train every model from scratch
- Need millions/billions of labeled examples
- Requires massive compute (weeks/months on GPUs)
- Only large companies can afford it

**With Transfer Learning:**
- Start with a pre-trained model (someone already spent $100M+ training it)
- Fine-tune on your specific task with much less data (100s-1000s of examples)
- Achieve state-of-the-art results quickly
- Accessible to individuals and small teams

## How It Works

```
Step 1: Pre-training (done by large AI labs)
  Massive dataset → Train foundation model → General knowledge

Step 2: Fine-tuning (done by you)
  Foundation model + Your small dataset → Fine-tune → Specialized model

Step 3: Deployment
  Specialized model → Your application / agent
```

## Types of Transfer Learning

### 1. Feature Extraction
Use the pre-trained model as a fixed feature extractor. Freeze all layers except the final classification head.
- **When to use**: Small dataset, task is similar to pre-training
- **Example**: Use ResNet features for custom image classification

### 2. Fine-Tuning
Unfreeze some or all layers and train on your data with a small learning rate.
- **When to use**: Moderate dataset, task differs somewhat from pre-training
- **Example**: Fine-tune BERT for sentiment analysis on product reviews

### 3. Domain Adaptation
Adapt a model from one domain to another (e.g., news text → medical text).
- **When to use**: Different domain but similar task structure
- **Example**: Adapt general LLM for legal document analysis

### 4. Prompt-Based Transfer (In-Context Learning)
Use an LLM's general knowledge through carefully crafted prompts — no weight updates needed.
- **When to use**: Zero or few examples available, fast iteration
- **Example**: GPT-4 answering domain-specific questions via prompt engineering

## Transfer Learning in Different Domains

| Domain | Pre-trained Model | Fine-tuning Task |
|--------|------------------|-----------------|
| NLP | BERT, GPT, Llama | Sentiment analysis, NER, QA |
| Vision | ResNet, ViT, CLIP | Medical imaging, defect detection |
| Speech | Whisper, wav2vec | Custom ASR, language ID |
| Code | CodeLlama, StarCoder | Code completion for specific languages |
| Multimodal | GPT-4V, LLaVA | Document understanding, visual QA |

## Transfer Learning for Agentic AI

Transfer learning is THE reason agentic AI is possible:

1. **Foundation models** (GPT-4, Claude) are pre-trained on vast data → general knowledge
2. **Fine-tuning** adapts them for specific agent behaviors → specialized agents
3. **In-context learning** (prompting) provides task-specific guidance → flexible agents
4. **RAG** adds external knowledge without retraining → knowledge-augmented agents

## Key Concepts

- **Foundation Model**: Large model pre-trained on broad data (GPT-4, Llama, BERT)
- **Catastrophic Forgetting**: Model forgets original knowledge when fine-tuned too aggressively
- **Learning Rate Warmup**: Start with very small learning rate when fine-tuning
- **Layer Freezing**: Keep early layers fixed, only train later layers
- **LoRA/QLoRA**: Efficient fine-tuning that only updates small adapter weights (covered in Section 07)
