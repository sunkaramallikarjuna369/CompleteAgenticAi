"""
Tool Use
========
Section 08

Demonstrates agent tool use: tool registry,
function calling, and tool selection.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import json

print("=" * 60)
print("AGENT TOOL USE")
print("=" * 60)

class ToolRegistry:
    def __init__(self):
        self.tools = {}
    def register(self, name, func, description, params):
        self.tools[name] = {"func": func, "desc": description, "params": params}
    def call(self, name, **kwargs):
        if name not in self.tools:
            return f"Tool '{name}' not found"
        return self.tools[name]["func"](**kwargs)
    def list_tools(self):
        return [{
            "name": n, "description": t["desc"], "parameters": t["params"]
        } for n, t in self.tools.items()]

# Register tools
registry = ToolRegistry()
registry.register("calculator", lambda expression: eval(expression),
    "Evaluate math expressions", {"expression": "string"})
registry.register("word_count", lambda text: len(text.split()),
    "Count words in text", {"text": "string"})
registry.register("reverse", lambda text: text[::-1],
    "Reverse a string", {"text": "string"})

print("  Available tools:")
for tool in registry.list_tools():
    print(f"    {tool['name']:15s}: {tool['description']}")

print("\n  Tool execution:")
tests = [
    ("calculator", {"expression": "2 ** 10"}),
    ("word_count", {"text": "AI agents use tools effectively"}),
    ("reverse", {"text": "hello"}),
]

for name, kwargs in tests:
    result = registry.call(name, **kwargs)
    print(f"    {name}({kwargs}) -> {result}")

print("\n  Tool Selection (based on query):")

def select_tool(query, tools):
    keywords = {
        "calculator": ["calculate", "math", "compute", "sum"],
        "word_count": ["count", "words", "length"],
        "reverse": ["reverse", "backward"],
    }
    for tool_name, kws in keywords.items():
        if any(kw in query.lower() for kw in kws):
            return tool_name
    return "unknown"

queries = ["Calculate 5 + 3", "Count words in this sentence", "Reverse the text"]
for q in queries:
    tool = select_tool(q, registry.tools)
    print(f"    '{q}' -> {tool}")

print("\nDone!")
