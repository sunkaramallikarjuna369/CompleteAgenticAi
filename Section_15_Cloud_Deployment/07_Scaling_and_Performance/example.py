"""
Scaling and Performance
=======================
Section 15

Demonstrates scaling strategies and performance
optimization for AI systems.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("SCALING & PERFORMANCE")
print("=" * 60)

# 1. Load Balancer
print("\n1. LOAD BALANCER SIMULATION")
print("-" * 40)

class LoadBalancer:
    def __init__(self, servers):
        self.servers = {s: {"load": 0, "requests": 0} for s in servers}
    def route(self, request, strategy="least_connections"):
        if strategy == "round_robin":
            server = list(self.servers.keys())[sum(s["requests"] for s in self.servers.values()) % len(self.servers)]
        else:
            server = min(self.servers, key=lambda s: self.servers[s]["load"])
        self.servers[server]["load"] += 1
        self.servers[server]["requests"] += 1
        return server

lb = LoadBalancer(["server-1", "server-2", "server-3"])
random.seed(42)
for i in range(12):
    server = lb.route(f"request-{i}")
    if i < 5:
        print(f"  Request {i+1:2d} -> {server}")

print(f"\n  Final distribution:")
for server, stats in lb.servers.items():
    bar = "#" * stats["requests"]
    print(f"    {server}: {bar} ({stats['requests']} requests)")

# 2. Caching
print("\n2. CACHE HIT RATES")
print("-" * 40)

class Cache:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.store = {}
        self.hits = 0
        self.misses = 0
    def get(self, key):
        if key in self.store:
            self.hits += 1
            return self.store[key]
        self.misses += 1
        return None
    def set(self, key, value):
        if len(self.store) >= self.capacity:
            oldest = next(iter(self.store))
            del self.store[oldest]
        self.store[key] = value
    def hit_rate(self):
        total = self.hits + self.misses
        return self.hits / total if total else 0

cache = Cache(50)
for i in range(200):
    key = f"query-{random.randint(0, 60)}"
    if cache.get(key) is None:
        cache.set(key, f"result-{key}")

print(f"  Cache hit rate: {cache.hit_rate():.1%}")
print(f"  Hits: {cache.hits}, Misses: {cache.misses}")

print("\nDone!")
