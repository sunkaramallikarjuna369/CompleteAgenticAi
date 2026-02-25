"""
System Prompts
==============
Section 06

Demonstrates system prompt design: persona setup,
boundary setting, and instruction formatting.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("SYSTEM PROMPT DESIGN")
print("=" * 60)

class SystemPromptBuilder:
    def __init__(self):
        self.sections = {}
    def set_role(self, role):
        self.sections["role"] = role
        return self
    def set_instructions(self, instructions):
        self.sections["instructions"] = instructions
        return self
    def set_constraints(self, constraints):
        self.sections["constraints"] = constraints
        return self
    def set_format(self, fmt):
        self.sections["output_format"] = fmt
        return self
    def build(self):
        parts = []
        if "role" in self.sections:
            parts.append(f"You are {self.sections['role']}.")
        if "instructions" in self.sections:
            parts.append(f"\nInstructions:\n{self.sections['instructions']}")
        if "constraints" in self.sections:
            parts.append(f"\nConstraints:\n{self.sections['constraints']}")
        if "output_format" in self.sections:
            parts.append(f"\nOutput Format:\n{self.sections['output_format']}")
        return "\n".join(parts)

# Build system prompts for different agents
print("\n1. CODE REVIEW AGENT")
print("-" * 40)
prompt1 = (SystemPromptBuilder()
    .set_role("an expert code reviewer specializing in Python")
    .set_instructions("- Review code for bugs, security issues, and best practices\n- Suggest improvements with examples")
    .set_constraints("- Only review Python code\n- Do not modify functionality\n- Be constructive")
    .set_format("## Issues\n[list issues]\n## Suggestions\n[list suggestions]")
    .build())
print(prompt1)

print("\n2. DATA ANALYST AGENT")
print("-" * 40)
prompt2 = (SystemPromptBuilder()
    .set_role("a data analyst who explains findings clearly")
    .set_instructions("- Analyze data and provide insights\n- Use statistical methods")
    .set_constraints("- Cite data sources\n- Express uncertainty when appropriate")
    .build())
print(prompt2)

# 3. Prompt testing
print("\n3. SYSTEM PROMPT VALIDATION")
print("-" * 40)

def validate_system_prompt(prompt):
    checks = {
        "Has role definition": any(w in prompt.lower() for w in ["you are", "act as"]),
        "Has instructions": "instruct" in prompt.lower() or "-" in prompt,
        "Reasonable length": 50 < len(prompt) < 5000,
        "Has constraints": any(w in prompt.lower() for w in ["do not", "constraint", "must"]),
    }
    for check, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {check}")
    return all(checks.values())

validate_system_prompt(prompt1)

print("\nDone!")
