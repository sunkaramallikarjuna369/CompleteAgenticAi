"""
Computer Vision
===============
Section 02

Demonstrates CV concepts: image representation,
convolution filters, and edge detection.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("1. IMAGE REPRESENTATION")
print("=" * 60)

image = [[random.randint(0, 255) for _ in range(8)] for _ in range(8)]
print("  8x8 Grayscale Image:")
for row in image:
    print("    " + " ".join(f"{p:3d}" for p in row))

print("\n" + "=" * 60)
print("2. CONVOLUTION FILTER")
print("=" * 60)

def convolve2d(image, kernel):
    h, w = len(image), len(image[0])
    kh, kw = len(kernel), len(kernel[0])
    ph, pw = kh // 2, kw // 2
    output = [[0] * w for _ in range(h)]
    for i in range(ph, h - ph):
        for j in range(pw, w - pw):
            val = 0
            for ki in range(kh):
                for kj in range(kw):
                    val += image[i-ph+ki][j-pw+kj] * kernel[ki][kj]
            output[i][j] = max(0, min(255, int(val)))
    return output

# Edge detection kernel (Sobel-X)
sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
edges = convolve2d(image, sobel_x)
print("  Sobel-X Edge Detection:")
for row in edges:
    print("    " + " ".join(f"{p:3d}" for p in row))

# Blur kernel
blur = [[1/9]*3]*3
blurred = convolve2d(image, blur)
print("\n  Box Blur:")
for row in blurred:
    print("    " + " ".join(f"{p:3d}" for p in row))

print("\nDone!")
