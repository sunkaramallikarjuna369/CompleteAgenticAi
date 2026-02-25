# CrewAI

## Overview
A framework for creating multi-agent systems where agents have specific roles and collaborate on tasks.

## Key Concepts
- **Agents**: Autonomous units with roles, goals, and backstories
- **Tasks**: Specific assignments with expected outputs
- **Crew**: A team of agents working together
- **Process**: Sequential or hierarchical task execution

## Example
```python
researcher = Agent(role="Researcher", goal="Find accurate information")
writer = Agent(role="Writer", goal="Create compelling content")
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
```

## For Agentic AI
- CrewAI makes multi-agent systems accessible
- Role-based design mirrors real team structures