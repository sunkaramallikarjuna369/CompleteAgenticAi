"""
Unsupervised Learning
=====================
Section 01

Demonstrates unsupervised learning: K-Means clustering,
PCA, and anomaly detection.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, math

print("=" * 60)
print("1. K-MEANS CLUSTERING")
print("=" * 60)

random.seed(42)

def kmeans(points, k=3, iterations=10):
    centroids = random.sample(points, k)
    for _ in range(iterations):
        clusters = {i: [] for i in range(k)}
        for p in points:
            dists = [math.sqrt(sum((a-b)**2 for a,b in zip(p,c))) for c in centroids]
            clusters[dists.index(min(dists))].append(p)
        for i in range(k):
            if clusters[i]:
                centroids[i] = [sum(dim)/len(clusters[i]) for dim in zip(*clusters[i])]
    return centroids, clusters

points = [[random.gauss(c[0], 1), random.gauss(c[1], 1)]
          for c in [(0,0), (5,5), (10,0)] for _ in range(15)]

centroids, clusters = kmeans(points, k=3)
for i, c in enumerate(centroids):
    print(f"  Cluster {i}: center=({c[0]:.1f}, {c[1]:.1f}), size={len(clusters[i])}")

print("\n" + "=" * 60)
print("2. SIMPLE PCA (2D -> 1D)")
print("=" * 60)

data = [[random.gauss(0, 3) + random.gauss(0, 1), random.gauss(0, 1)] for _ in range(50)]
mean_x = sum(p[0] for p in data) / len(data)
mean_y = sum(p[1] for p in data) / len(data)
centered = [[p[0]-mean_x, p[1]-mean_y] for p in data]

cov_xx = sum(p[0]**2 for p in centered) / len(centered)
cov_yy = sum(p[1]**2 for p in centered) / len(centered)
cov_xy = sum(p[0]*p[1] for p in centered) / len(centered)
print(f"  Original variance: x={cov_xx:.2f}, y={cov_yy:.2f}")
print(f"  Covariance: {cov_xy:.2f}")

print("\n" + "=" * 60)
print("3. ANOMALY DETECTION (Z-score)")
print("=" * 60)

data = [random.gauss(50, 5) for _ in range(100)]
data.extend([100, 5, 95])
mean = sum(data) / len(data)
std = math.sqrt(sum((x-mean)**2 for x in data) / len(data))
anomalies = [(i, x) for i, x in enumerate(data) if abs(x - mean) > 2 * std]
print(f"  Mean={mean:.1f}, Std={std:.1f}")
print(f"  Anomalies (|z|>2): {len(anomalies)}")
for idx, val in anomalies:
    print(f"    [{idx}] value={val:.1f}, z-score={(val-mean)/std:.1f}")

print("\nDone!")
