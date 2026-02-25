"""
Image Generation Concepts
=========================
Section 05

Demonstrates image generation concepts: noise schedules,
diffusion process, and ASCII visualization.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("IMAGE GENERATION (DIFFUSION CONCEPTS)")
print("=" * 60)

print("\n1. NOISE SCHEDULES")
print("-" * 40)

def linear_schedule(T, beta_start=0.0001, beta_end=0.02):
    return [beta_start + (beta_end - beta_start) * t / T for t in range(T)]

def cosine_schedule(T):
    return [1 - math.cos((t/T + 0.008) / 1.008 * math.pi/2)**2 for t in range(T)]

T = 10
linear = linear_schedule(T)
cosine = cosine_schedule(T)

print(f"  {'Step':>4} {'Linear':>8} {'Cosine':>8}")
for t in range(T):
    print(f"  {t:>4} {linear[t]:>8.4f} {cosine[t]:>8.4f}")

print("\n2. FORWARD DIFFUSION (Adding Noise)")
print("-" * 40)

random.seed(42)
image = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]
print("  Original:")
for row in image:
    print("    " + " ".join(str(v) for v in row))

noisy = [[max(0, min(9, v + random.randint(-3, 3))) for v in row] for row in image]
print("\n  After noise (t=5):")
for row in noisy:
    print("    " + " ".join(str(v) for v in row))

pure_noise = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]
print("\n  Pure noise (t=T):")
for row in pure_noise:
    print("    " + " ".join(str(v) for v in row))

print("\nDone!")
