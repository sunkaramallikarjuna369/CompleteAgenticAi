"""
LangChain Framework
===================
Section 09

Demonstrates LangChain concepts: chains, prompts,
memory, and agents (simulation).

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("LANGCHAIN FRAMEWORK CONCEPTS")
print("=" * 60)

# 1. Chain Pattern
print("\n1. CHAIN PATTERN")
print("-" * 40)

class Chain:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def run(self, input_data):
        return self.func(input_data)

class SequentialChain:
    def __init__(self, chains):
        self.chains = chains
    def run(self, input_data):
        data = input_data
        for chain in self.chains:
            data = chain.run(data)
            print(f"    [{chain.name}] -> {str(data)[:50]}")
        return data

pipeline = SequentialChain([
    Chain("format", lambda x: x.strip().lower()),
    Chain("tokenize", lambda x: x.split()),
    Chain("count", lambda x: {"tokens": len(x), "words": x}),
])

result = pipeline.run("  Hello World From LangChain  ")
print(f"  Final: {result}")

# 2. Prompt Templates
print("\n2. PROMPT TEMPLATES")
print("-" * 40)

class PromptTemplate:
    def __init__(self, template, input_vars):
        self.template = template
        self.input_vars = input_vars
    def format(self, **kwargs):
        result = self.template
        for var in self.input_vars:
            result = result.replace(f"{{{var}}}", str(kwargs.get(var, "")))
        return result

tmpl = PromptTemplate(
    "You are a {role}. Answer the question about {topic}:\n{question}",
    ["role", "topic", "question"])

prompt = tmpl.format(role="Python expert", topic="async programming",
                     question="What is asyncio?")
print(f"  {prompt}")

# 3. Agent with Tools
print("\n3. AGENT WITH TOOLS")
print("-" * 40)

class LangChainAgent:
    def __init__(self, tools):
        self.tools = {t["name"]: t for t in tools}
    def plan(self, query):
        for name, tool in self.tools.items():
            if any(kw in query.lower() for kw in tool.get("keywords", [])):
                return name
        return "direct_answer"
    def run(self, query):
        tool_name = self.plan(query)
        print(f"    Query: {query}")
        print(f"    Tool selected: {tool_name}")
        if tool_name in self.tools:
            result = self.tools[tool_name]["func"](query)
            print(f"    Result: {result}")
        return "Done"

tools = [
    {"name": "search", "keywords": ["find", "search", "look up"],
     "func": lambda q: "Found 5 relevant results"},
    {"name": "calculator", "keywords": ["calculate", "compute", "math"],
     "func": lambda q: "42"},
]

agent = LangChainAgent(tools)
agent.run("Search for AI agent tutorials")
agent.run("Calculate the sum of 1 to 100")

print("\nDone!")
