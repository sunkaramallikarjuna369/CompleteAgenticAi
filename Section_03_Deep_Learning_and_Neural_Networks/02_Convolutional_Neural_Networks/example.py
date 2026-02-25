"""
Convolutional Neural Networks
=============================
Section 03

Demonstrates CNN concepts: Conv2D layer,
max pooling, and feature maps.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("1. CONV2D LAYER")
print("=" * 60)

def conv2d(image, kernel, stride=1):
    ih, iw = len(image), len(image[0])
    kh, kw = len(kernel), len(kernel[0])
    oh = (ih - kh) // stride + 1
    ow = (iw - kw) // stride + 1
    output = [[0]*ow for _ in range(oh)]
    for i in range(oh):
        for j in range(ow):
            val = 0
            for ki in range(kh):
                for kj in range(kw):
                    val += image[i*stride+ki][j*stride+kj] * kernel[ki][kj]
            output[i][j] = max(0, val)  # ReLU
    return output

random.seed(42)
image = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]
kernel = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]

print("  Input (6x6):")
for row in image:
    print("    " + " ".join(f"{v}" for v in row))

result = conv2d(image, kernel)
print(f"\n  After Conv2D (3x3 kernel, ReLU):")
for row in result:
    print("    " + " ".join(f"{v:2d}" for v in row))

print("\n" + "=" * 60)
print("2. MAX POOLING")
print("=" * 60)

def max_pool(feature_map, pool_size=2):
    h, w = len(feature_map), len(feature_map[0])
    oh, ow = h // pool_size, w // pool_size
    output = [[0]*ow for _ in range(oh)]
    for i in range(oh):
        for j in range(ow):
            vals = []
            for pi in range(pool_size):
                for pj in range(pool_size):
                    vals.append(feature_map[i*pool_size+pi][j*pool_size+pj])
            output[i][j] = max(vals)
    return output

pooled = max_pool(result)
print("  After 2x2 Max Pooling:")
for row in pooled:
    print("    " + " ".join(f"{v:2d}" for v in row))

print("\n" + "=" * 60)
print("3. CNN ARCHITECTURE SUMMARY")
print("=" * 60)
layers = [
    ("Input", "32x32x3"),
    ("Conv2D + ReLU", "30x30x16"),
    ("MaxPool", "15x15x16"),
    ("Conv2D + ReLU", "13x13x32"),
    ("MaxPool", "6x6x32"),
    ("Flatten", "1152"),
    ("Dense + Softmax", "10"),
]
for name, shape in layers:
    print(f"  {name:20s} -> {shape}")

print("\nDone!")
