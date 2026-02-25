"""
Output Formatting
=================
Section 06

Demonstrates output formatting: JSON schemas,
structured responses, and parsers.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import json, re

print("=" * 60)
print("OUTPUT FORMATTING")
print("=" * 60)

# 1. JSON Output Schema
print("\n1. JSON OUTPUT SCHEMA")
print("-" * 40)

class OutputSchema:
    def __init__(self, name):
        self.name = name
        self.fields = []
    def add_field(self, name, type_name, required=True, description=""):
        self.fields.append({"name": name, "type": type_name, "required": required, "desc": description})
    def to_prompt(self):
        lines = [f"Respond in the following JSON format:"]
        lines.append("{")
        for f in self.fields:
            req = "required" if f["required"] else "optional"
            lines.append(f'  "{f["name"]}": <{f["type"]}>,  // {f["desc"]} ({req})')
        lines.append("}")
        return "\n".join(lines)
    def validate(self, data):
        errors = []
        for f in self.fields:
            if f["required"] and f["name"] not in data:
                errors.append(f"Missing required field: {f['name']}")
        return errors

schema = OutputSchema("Analysis")
schema.add_field("sentiment", "string", True, "positive/negative/neutral")
schema.add_field("confidence", "float", True, "0.0 to 1.0")
schema.add_field("entities", "list[string]", False, "Named entities found")

print(schema.to_prompt())

# Validate sample output
sample = {"sentiment": "positive", "confidence": 0.92, "entities": ["Python", "AI"]}
errors = schema.validate(sample)
print(f"\n  Validation: {'PASS' if not errors else errors}")

# 2. Structured Response Parser
print("\n2. RESPONSE PARSER")
print("-" * 40)

class ResponseParser:
    def parse_json(self, text):
        match = re.search(r'\{[^{}]*\}', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                return None
        return None

    def parse_list(self, text):
        return re.findall(r'^\s*[-*]\s*(.+)$', text, re.MULTILINE)

    def parse_key_value(self, text):
        return dict(re.findall(r'(\w+):\s*(.+)', text))

parser = ResponseParser()

test_response = 'Here is the result: {"sentiment": "positive", "score": 0.9}'
parsed = parser.parse_json(test_response)
print(f"  Parsed JSON: {parsed}")

test_list = "Key points:\n- AI is transforming industries\n- Agents are autonomous\n- LLMs are foundation"
parsed_list = parser.parse_list(test_list)
print(f"  Parsed list: {parsed_list}")

print("\nDone!")
