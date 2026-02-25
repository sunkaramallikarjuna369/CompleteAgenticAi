"""
Agent Observability
===================
Section 12

Demonstrates observability: logging, tracing,
and metrics collection for agents.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import json, random, time
from datetime import datetime

print("=" * 60)
print("AGENT OBSERVABILITY")
print("=" * 60)

# 1. Structured Logging
print("\n1. STRUCTURED LOGGING")
print("-" * 40)

class AgentLogger:
    def __init__(self, agent_name):
        self.agent = agent_name
        self.logs = []
    def log(self, level, message, **kwargs):
        entry = {"ts": datetime.now().isoformat(), "agent": self.agent,
                 "level": level, "msg": message, **kwargs}
        self.logs.append(entry)
        print(f"  {json.dumps(entry)}")

logger = AgentLogger("research-agent")
logger.log("INFO", "Agent started", version="1.0")
logger.log("INFO", "Processing query", query="AI trends", tokens=150)
logger.log("WARN", "High latency", latency_ms=2500)
logger.log("INFO", "Task completed", duration_s=5.2)

# 2. Distributed Tracing
print("\n2. DISTRIBUTED TRACING")
print("-" * 40)

class Span:
    def __init__(self, name, trace_id, parent_id=None):
        self.name = name
        self.trace_id = trace_id
        self.span_id = f"span-{random.randint(1000,9999)}"
        self.parent_id = parent_id
        self.start = time.time()
        self.duration = 0
    def end(self, duration):
        self.duration = duration

class Tracer:
    def __init__(self):
        self.spans = []
    def start_span(self, name, trace_id, parent_id=None):
        span = Span(name, trace_id, parent_id)
        self.spans.append(span)
        return span
    def show(self):
        for s in self.spans:
            indent = "  " if s.parent_id else ""
            print(f"  {indent}[{s.span_id}] {s.name} ({s.duration}ms)")

random.seed(42)
tracer = Tracer()
root = tracer.start_span("agent.process", "trace-001")
root.end(150)
child1 = tracer.start_span("retrieve.docs", "trace-001", root.span_id)
child1.end(45)
child2 = tracer.start_span("llm.generate", "trace-001", root.span_id)
child2.end(95)

tracer.show()

# 3. Metrics
print("\n3. METRICS DASHBOARD")
print("-" * 40)

metrics = {
    "requests_total": 1250,
    "errors_total": 23,
    "avg_latency_ms": 340,
    "tokens_used": 450000,
    "cache_hit_rate": 0.72,
}

for name, value in metrics.items():
    if isinstance(value, float):
        print(f"  {name:25s}: {value:.1%}")
    else:
        print(f"  {name:25s}: {value:,}")

print(f"\n  Error rate: {metrics['errors_total']/metrics['requests_total']:.1%}")

print("\nDone!")
