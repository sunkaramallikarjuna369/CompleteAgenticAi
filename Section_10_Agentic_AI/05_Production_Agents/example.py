"""
Production Agents
=================
Section 10

Demonstrates production agent concepts: reliability,
monitoring, and deployment patterns.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random, time

print("=" * 60)
print("PRODUCTION AGENTS")
print("=" * 60)

# 1. Retry Logic
print("\n1. RETRY WITH BACKOFF")
print("-" * 40)

class RetryHandler:
    def __init__(self, max_retries=3, base_delay=0.1):
        self.max_retries = max_retries
        self.base_delay = base_delay

    def execute(self, func, *args):
        for attempt in range(self.max_retries + 1):
            try:
                result = func(*args)
                print(f"    Attempt {attempt + 1}: SUCCESS")
                return result
            except Exception as e:
                delay = self.base_delay * (2 ** attempt)
                print(f"    Attempt {attempt + 1}: FAILED ({e}), retry in {delay:.1f}s")
                if attempt == self.max_retries:
                    raise

random.seed(42)
retry = RetryHandler(max_retries=3)

def flaky_api():
    if random.random() < 0.6:
        raise Exception("API timeout")
    return "API response data"

try:
    result = retry.execute(flaky_api)
except Exception:
    print("    All retries exhausted")

# 2. Rate Limiter
print("\n2. RATE LIMITER")
print("-" * 40)

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = []

    def allow(self):
        now = time.time()
        self.requests = [t for t in self.requests if now - t < self.window]
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False

limiter = RateLimiter(max_requests=5, window_seconds=1)
for i in range(8):
    allowed = limiter.allow()
    status = "ALLOWED" if allowed else "BLOCKED"
    print(f"    Request {i+1}: {status}")

# 3. Health Check
print("\n3. AGENT HEALTH CHECK")
print("-" * 40)

class AgentHealthCheck:
    def __init__(self):
        self.checks = {}
    def add_check(self, name, fn):
        self.checks[name] = fn
    def run(self):
        results = {}
        for name, fn in self.checks.items():
            try:
                results[name] = "healthy" if fn() else "unhealthy"
            except Exception:
                results[name] = "error"
        return results

health = AgentHealthCheck()
health.add_check("memory", lambda: True)
health.add_check("tools", lambda: True)
health.add_check("llm_connection", lambda: True)

results = health.run()
all_healthy = all(v == "healthy" for v in results.values())
print(f"  Status: {'HEALTHY' if all_healthy else 'UNHEALTHY'}")
for name, status in results.items():
    print(f"    {name:20s}: {status}")

print("\nDone!")
