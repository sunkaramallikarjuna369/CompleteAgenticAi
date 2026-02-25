# Agent Design Patterns

## ReAct (Reasoning + Acting)
The most fundamental agent pattern. Interleave thinking with actions.
```
Thought -> Action -> Observation -> Thought -> Action -> ... -> Answer
```

## Plan-and-Execute
Create a full plan first, then execute steps.
```
Plan: [Step 1, Step 2, Step 3] -> Execute Step 1 -> Execute Step 2 -> ...
```

## Reflection
Agent evaluates its own output and iterates.
```
Generate -> Evaluate -> Improve -> Evaluate -> ... -> Final
```

## Tool Selection
Agent chooses the right tool for each subtask.

## Human-in-the-Loop
Agent requests human approval for critical decisions.

## For Agentic AI
- ReAct is the default pattern for most agents
- Plan-and-Execute for complex multi-step tasks
- Reflection for quality-critical applications