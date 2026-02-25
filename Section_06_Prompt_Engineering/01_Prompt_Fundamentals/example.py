"""
Prompt Fundamentals
===================
Section 06

Demonstrates prompt engineering basics: templates,
role-based prompts, and structured formatting.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("PROMPT FUNDAMENTALS")
print("=" * 60)

class PromptTemplate:
    def __init__(self, template):
        self.template = template
    def format(self, **kwargs):
        result = self.template
        for key, value in kwargs.items():
            result = result.replace(f"{{{key}}}", str(value))
        return result

# 1. Basic templates
print("\n1. PROMPT TEMPLATES")
print("-" * 40)

templates = {
    "classify": PromptTemplate("Classify the following text as {categories}:\n\nText: {text}\nCategory:"),
    "summarize": PromptTemplate("Summarize the following in {length}:\n\n{text}\n\nSummary:"),
    "translate": PromptTemplate("Translate from {source} to {target}:\n\n{text}\n\nTranslation:"),
}

for name, tmpl in templates.items():
    if name == "classify":
        prompt = tmpl.format(categories="positive/negative/neutral", text="I love this product!")
    elif name == "summarize":
        prompt = tmpl.format(length="one sentence", text="AI agents are autonomous systems...")
    else:
        prompt = tmpl.format(source="English", target="French", text="Hello world")
    print(f"  [{name}]:")
    print(f"  {prompt}\n")

# 2. Role-based prompts
print("2. ROLE-BASED PROMPTS")
print("-" * 40)

roles = [
    {"role": "system", "content": "You are an expert Python developer."},
    {"role": "user", "content": "How do I read a CSV file?"},
    {"role": "assistant", "content": "Use the csv module: import csv ..."},
]
for msg in roles:
    print(f"  [{msg['role']:10s}] {msg['content'][:50]}")

# 3. Prompt scoring
print("\n3. PROMPT QUALITY SCORING")
print("-" * 40)

def score_prompt(prompt):
    score = 0
    if len(prompt) > 20: score += 1
    if any(w in prompt.lower() for w in ["step", "example", "explain"]): score += 2
    if "?" in prompt or ":" in prompt: score += 1
    if len(prompt.split()) > 10: score += 1
    return min(score, 5)

test_prompts = [
    "Fix this",
    "Explain how transformers work step by step with examples:",
    "What are the key differences between CNN and RNN architectures?",
]
for p in test_prompts:
    s = score_prompt(p)
    bar = "#" * s
    print(f"  Score {s}/5 {bar:5s} | {p[:55]}")

print("\nDone!")
