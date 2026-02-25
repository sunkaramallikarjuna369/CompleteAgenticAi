# Advanced Prompt Techniques

## Chain-of-Thought (CoT)
"Think step by step" - asking the model to show its reasoning.

## Self-Consistency
Generate multiple CoT paths, take majority vote.

## Tree of Thought
Explore multiple reasoning branches, evaluate each.

## ReAct (Reasoning + Acting)
Interleave reasoning with actions (tool calls).
```
Thought: I need to find the weather
Action: search("weather in NYC")
Observation: 72F, sunny
Thought: Now I can answer
Answer: It's 72F and sunny in NYC
```

## For Agentic AI
- ReAct is THE prompting pattern for agents
- CoT improves reasoning quality
- These techniques define how agents think