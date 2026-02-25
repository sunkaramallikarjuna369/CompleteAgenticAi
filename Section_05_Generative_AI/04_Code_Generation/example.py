"""
Code Generation
===============
Section 05

Demonstrates code generation concepts: AST building,
code templates, and program synthesis.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("CODE GENERATION CONCEPTS")
print("=" * 60)

# 1. AST Builder
print("\n1. ABSTRACT SYNTAX TREE (AST)")
print("-" * 40)

class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children or []
    def to_code(self, indent=0):
        prefix = "    " * indent
        if self.type == "function":
            params = ", ".join(c.to_code() for c in self.children if c.type == "param")
            body = "\n".join(c.to_code(indent+1) for c in self.children if c.type != "param")
            return f"{prefix}def {self.value}({params}):\n{body}"
        elif self.type == "param":
            return self.value
        elif self.type == "return":
            return f"{prefix}return {self.children[0].to_code()}"
        elif self.type == "expr":
            return self.value
        elif self.type == "assign":
            return f"{prefix}{self.value} = {self.children[0].to_code()}"
        return f"{prefix}{self.value}"

# Build AST for: def add(a, b): return a + b
func = ASTNode("function", "add", [
    ASTNode("param", "a"),
    ASTNode("param", "b"),
    ASTNode("return", children=[ASTNode("expr", "a + b")])
])

print("  Generated code:")
print(func.to_code())

# 2. Code Templates
print("\n2. CODE TEMPLATES")
print("-" * 40)

class CodeTemplate:
    def __init__(self, template):
        self.template = template
    def generate(self, **kwargs):
        code = self.template
        for key, value in kwargs.items():
            code = code.replace(f"{{{key}}}", str(value))
        return code

api_template = CodeTemplate(
"""from fastapi import FastAPI
app = FastAPI()

@app.get("/{endpoint}")
def {function_name}():
    return {{"message": "{response}"}}""")

code = api_template.generate(
    endpoint="health",
    function_name="health_check",
    response="OK"
)
print("  Generated API:")
print(code)

print("\nDone!")
