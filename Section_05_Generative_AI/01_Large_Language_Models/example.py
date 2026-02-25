"""
Large Language Models
=====================
Section 05

Demonstrates LLM concepts: n-gram model, tokenization,
and next-word prediction.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random
from collections import Counter

print("=" * 60)
print("1. N-GRAM LANGUAGE MODEL")
print("=" * 60)

text = "the cat sat on the mat the cat ate the fish the dog sat on the mat"
words = text.split()

def build_ngram(words, n=2):
    model = {}
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        if key not in model:
            model[key] = []
        model[key].append(next_word)
    return model

bigram = build_ngram(words, 2)
print("  Bigram model:")
for key, values in sorted(bigram.items()):
    counts = Counter(values)
    print(f"    {' '.join(key):15s} -> {dict(counts)}")

print("\n" + "=" * 60)
print("2. TEXT GENERATION")
print("=" * 60)

random.seed(42)
def generate(model, start, n_words=10):
    result = list(start)
    for _ in range(n_words):
        key = tuple(result[-2:])
        if key in model:
            result.append(random.choice(model[key]))
        else:
            break
    return " ".join(result)

for _ in range(3):
    text = generate(bigram, ("the", "cat"), 8)
    print(f"  {text}")

print("\n" + "=" * 60)
print("3. LLM ARCHITECTURE OVERVIEW")
print("=" * 60)

components = [
    ("Tokenizer", "Splits text into tokens (BPE/WordPiece)"),
    ("Embedding", "Converts tokens to dense vectors"),
    ("Transformer Blocks", "Self-attention + FFN layers"),
    ("Layer Norm", "Normalizes activations"),
    ("Output Head", "Projects to vocabulary logits"),
]
for name, desc in components:
    print(f"  {name:22s}: {desc}")

print("\nDone!")
