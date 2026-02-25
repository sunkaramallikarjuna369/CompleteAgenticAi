"""
Semantic Kernel
===============
Section 09

Demonstrates Semantic Kernel concepts: plugins,
functions, and kernel orchestration.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("SEMANTIC KERNEL CONCEPTS")
print("=" * 60)

class KernelFunction:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func
    def invoke(self, **kwargs):
        return self.func(**kwargs)

class Plugin:
    def __init__(self, name):
        self.name = name
        self.functions = {}
    def add_function(self, func):
        self.functions[func.name] = func

class Kernel:
    def __init__(self):
        self.plugins = {}
    def add_plugin(self, plugin):
        self.plugins[plugin.name] = plugin
    def invoke(self, plugin_name, function_name, **kwargs):
        plugin = self.plugins.get(plugin_name)
        if not plugin:
            return f"Plugin '{plugin_name}' not found"
        func = plugin.functions.get(function_name)
        if not func:
            return f"Function '{function_name}' not found"
        return func.invoke(**kwargs)
    def list_functions(self):
        for pname, plugin in self.plugins.items():
            for fname, func in plugin.functions.items():
                print(f"    {pname}.{fname}: {func.description}")

# Build kernel
kernel = Kernel()

# Text plugin
text_plugin = Plugin("TextPlugin")
text_plugin.add_function(KernelFunction("summarize", "Summarize text",
    lambda text="", **kw: f"Summary of {len(text.split())} words: {text[:30]}..."))
text_plugin.add_function(KernelFunction("translate", "Translate text",
    lambda text="", target="", **kw: f"[{target}] {text}"))
kernel.add_plugin(text_plugin)

# Math plugin
math_plugin = Plugin("MathPlugin")
math_plugin.add_function(KernelFunction("add", "Add numbers",
    lambda a=0, b=0, **kw: float(a) + float(b)))
math_plugin.add_function(KernelFunction("multiply", "Multiply numbers",
    lambda a=0, b=0, **kw: float(a) * float(b)))
kernel.add_plugin(math_plugin)

print("  Available functions:")
kernel.list_functions()

print("\n  Invocations:")
results = [
    kernel.invoke("TextPlugin", "summarize", text="AI agents are autonomous systems that can plan reason and act"),
    kernel.invoke("MathPlugin", "add", a=42, b=58),
    kernel.invoke("MathPlugin", "multiply", a=7, b=6),
]
for r in results:
    print(f"    -> {r}")

print("\nDone!")
