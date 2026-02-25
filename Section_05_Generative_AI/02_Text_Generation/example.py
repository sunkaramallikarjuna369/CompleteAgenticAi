"""
Text Generation
===============
Section 05

Demonstrates text generation: greedy, top-k,
and nucleus (top-p) sampling.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("TEXT GENERATION STRATEGIES")
print("=" * 60)

def softmax(logits, temperature=1.0):
    scaled = [l / temperature for l in logits]
    m = max(scaled)
    exps = [math.exp(s - m) for s in scaled]
    total = sum(exps)
    return [e / total for e in exps]

vocab = ["the", "cat", "sat", "on", "mat", "dog", "ate", "fish", "ran", "fast"]
random.seed(42)

def sample_token(vocab, logits, strategy="greedy", k=3, p=0.9, temp=1.0):
    probs = softmax(logits, temp)
    if strategy == "greedy":
        return vocab[probs.index(max(probs))]
    elif strategy == "top_k":
        top_indices = sorted(range(len(probs)), key=lambda i: -probs[i])[:k]
        top_probs = [probs[i] for i in top_indices]
        total = sum(top_probs)
        top_probs = [p / total for p in top_probs]
        r = random.random()
        cumsum = 0
        for i, prob in zip(top_indices, top_probs):
            cumsum += prob
            if r <= cumsum:
                return vocab[i]
    elif strategy == "nucleus":
        sorted_idx = sorted(range(len(probs)), key=lambda i: -probs[i])
        cumsum = 0
        selected = []
        for i in sorted_idx:
            cumsum += probs[i]
            selected.append(i)
            if cumsum >= p:
                break
        sel_probs = [probs[i] for i in selected]
        total = sum(sel_probs)
        sel_probs = [sp / total for sp in sel_probs]
        r = random.random()
        cs = 0
        for i, sp in zip(selected, sel_probs):
            cs += sp
            if r <= cs:
                return vocab[i]
    return vocab[0]

logits = [2.5, 1.8, 1.2, 0.8, 0.5, 0.3, 0.2, 0.1, -0.1, -0.5]

for strategy in ["greedy", "top_k", "nucleus"]:
    tokens = []
    for _ in range(6):
        t = sample_token(vocab, logits, strategy=strategy, k=3, p=0.9)
        tokens.append(t)
        random.seed(random.randint(0, 1000))
    print(f"  {strategy:10s}: {' '.join(tokens)}")

print("\nDone!")
