"""
CrewAI Framework
================
Section 09

Demonstrates CrewAI concepts: agents, tasks,
crews, and collaborative execution.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""


print("=" * 60)
print("CREWAI CONCEPTS")
print("=" * 60)

class Agent:
    def __init__(self, role, goal, backstory=""):
        self.role = role
        self.goal = goal
        self.backstory = backstory
    def execute(self, task_description):
        return f"[{self.role}] Completed: {task_description}"

class Task:
    def __init__(self, description, agent, expected_output=""):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output
        self.result = None

class Crew:
    def __init__(self, agents, tasks, verbose=True):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose
    def kickoff(self):
        results = []
        for task in self.tasks:
            result = task.agent.execute(task.description)
            task.result = result
            results.append(result)
            if self.verbose:
                print(f"  {result}")
        return results

# Create crew
researcher = Agent("Researcher", "Find latest AI trends", "Expert at gathering information")
writer = Agent("Writer", "Create compelling content", "Skilled technical writer")
reviewer = Agent("Reviewer", "Ensure quality and accuracy", "Detail-oriented editor")

tasks = [
    Task("Research the latest developments in AI agents", researcher),
    Task("Write a comprehensive article about AI agents", writer),
    Task("Review the article for accuracy and clarity", reviewer),
]

print("  Crew Members:")
for a in [researcher, writer, reviewer]:
    print(f"    {a.role:12s}: {a.goal}")

print("\n  Executing tasks:")
crew = Crew([researcher, writer, reviewer], tasks)
results = crew.kickoff()

print(f"\n  Tasks completed: {len(results)}")

print("\nDone!")
