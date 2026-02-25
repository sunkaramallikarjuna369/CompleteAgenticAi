"""
Data Processing Pipelines
=========================
Section 04

Demonstrates ETL pipelines: extraction, transformation,
loading, and pipeline orchestration.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import json, random

print("=" * 60)
print("1. ETL PIPELINE")
print("=" * 60)

class Pipeline:
    def __init__(self):
        self.steps = []
    def add_step(self, name, func):
        self.steps.append((name, func))
        return self
    def run(self, data):
        for name, func in self.steps:
            data = func(data)
            print(f"  [{name}] -> {len(data) if isinstance(data, list) else type(data).__name__}")
        return data

random.seed(42)
raw_data = [{"name": f"Item_{i}", "value": random.gauss(100, 30),
             "category": random.choice(["A", "B", "C"])} for i in range(20)]

pipe = Pipeline()
pipe.add_step("Extract", lambda d: d)
pipe.add_step("Clean", lambda d: [x for x in d if x["value"] > 50])
pipe.add_step("Transform", lambda d: [{**x, "value": round(x["value"], 2)} for x in d])
pipe.add_step("Validate", lambda d: [x for x in d if x["name"] and x["value"] > 0])

result = pipe.run(raw_data)
print(f"\n  Input: {len(raw_data)} records")
print(f"  Output: {len(result)} records")
print(f"  Sample: {result[0]}")

print("\n" + "=" * 60)
print("2. DATA VALIDATION")
print("=" * 60)

class DataValidator:
    def __init__(self):
        self.rules = []
    def add_rule(self, name, check):
        self.rules.append((name, check))
    def validate(self, records):
        errors = []
        for i, rec in enumerate(records):
            for name, check in self.rules:
                if not check(rec):
                    errors.append(f"  Record {i}: Failed '{name}'")
        return errors

validator = DataValidator()
validator.add_rule("has_name", lambda r: bool(r.get("name")))
validator.add_rule("positive_value", lambda r: r.get("value", 0) > 0)
validator.add_rule("valid_category", lambda r: r.get("category") in ("A", "B", "C"))

errors = validator.validate(result)
print(f"  Validation: {len(result)} records, {len(errors)} errors")

print("\nDone!")
