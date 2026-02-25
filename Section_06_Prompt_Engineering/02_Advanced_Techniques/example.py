"""
Advanced Prompt Techniques
==========================
Section 06

Demonstrates advanced techniques: chain-of-thought,
few-shot learning, and prompt chaining.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("ADVANCED PROMPT TECHNIQUES")
print("=" * 60)

# 1. Chain of Thought
print("\n1. CHAIN-OF-THOUGHT PROMPTING")
print("-" * 40)

class ChainOfThought:
    def __init__(self):
        self.steps = []
    def think(self, step):
        self.steps.append(step)
        return self
    def conclude(self):
        print("  Reasoning chain:")
        for i, step in enumerate(self.steps, 1):
            print(f"    Step {i}: {step}")
        return self.steps[-1] if self.steps else "No conclusion"

cot = ChainOfThought()
cot.think("The problem asks for the sum of even numbers from 1-10")
cot.think("Even numbers: 2, 4, 6, 8, 10")
cot.think("Sum = 2 + 4 + 6 + 8 + 10")
cot.think("Sum = 30")
result = cot.conclude()
print(f"  Answer: {result}")

# 2. Few-Shot Learning
print("\n2. FEW-SHOT PROMPTING")
print("-" * 40)

class FewShotPrompt:
    def __init__(self, task_description):
        self.task = task_description
        self.examples = []
    def add_example(self, input_text, output_text):
        self.examples.append((input_text, output_text))
    def build(self, query):
        parts = [self.task + "\n"]
        for inp, out in self.examples:
            parts.append(f"Input: {inp}\nOutput: {out}\n")
        parts.append(f"Input: {query}\nOutput:")
        return "\n".join(parts)

fs = FewShotPrompt("Classify sentiment as positive, negative, or neutral.")
fs.add_example("I love this!", "positive")
fs.add_example("This is terrible.", "negative")
fs.add_example("It's okay.", "neutral")

prompt = fs.build("This product is amazing!")
print(f"  Generated prompt:\n  {prompt}")

# 3. Prompt Chaining
print("\n3. PROMPT CHAINING")
print("-" * 40)

class PromptChain:
    def __init__(self):
        self.chain = []
    def add(self, name, transform):
        self.chain.append((name, transform))
        return self
    def run(self, input_data):
        data = input_data
        for name, transform in self.chain:
            data = transform(data)
            print(f"  [{name}] -> {str(data)[:60]}")
        return data

chain = PromptChain()
chain.add("Extract entities", lambda t: ["Python", "AI", "Machine Learning"])
chain.add("Categorize", lambda entities: {e: "Technology" for e in entities})
chain.add("Generate summary", lambda cats: f"Found {len(cats)} technology entities")

result = chain.run("Python is used in AI and Machine Learning")
print(f"  Final: {result}")

print("\nDone!")
