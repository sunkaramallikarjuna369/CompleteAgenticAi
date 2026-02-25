# Introduction to Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) is the science and engineering of creating intelligent machines and software that can perform tasks typically requiring human intelligence. These tasks include reasoning, learning, problem-solving, perception, language understanding, and decision-making.

## A Brief History of AI

| Era | Period | Key Milestones |
|-----|--------|---------------|
| **Birth of AI** | 1950s | Alan Turing's "Computing Machinery and Intelligence", Dartmouth Conference (1956) |
| **Early Enthusiasm** | 1960s | ELIZA chatbot, General Problem Solver, Perceptrons |
| **First AI Winter** | 1970s | Limitations exposed, funding cuts, Lighthill Report |
| **Expert Systems** | 1980s | Rule-based systems, MYCIN, R1/XCON for industry |
| **Second AI Winter** | Late 1980s-90s | Expert systems proved brittle, market collapse |
| **ML Renaissance** | 2000s | Statistical ML, SVMs, Random Forests, data explosion |
| **Deep Learning Era** | 2012+ | AlexNet, GPUs, ImageNet breakthrough |
| **Generative AI** | 2020+ | GPT-3/4, DALL-E, Stable Diffusion, ChatGPT |
| **Agentic AI** | 2024+ | Autonomous AI agents, multi-agent systems, tool use |

## Types of AI

### By Capability

1. **Narrow AI (ANI - Artificial Narrow Intelligence)**
   - Designed for a specific task
   - All current AI systems fall here
   - Examples: Siri, Chess engines, Image classifiers, ChatGPT

2. **General AI (AGI - Artificial General Intelligence)**
   - Human-level intelligence across all domains
   - Can transfer learning between tasks
   - Does not exist yet — active research goal

3. **Super AI (ASI - Artificial Super Intelligence)**
   - Surpasses human intelligence in every way
   - Theoretical concept
   - Raises significant ethical and existential concerns

### By Functionality

1. **Reactive Machines** — No memory, respond to current inputs only (e.g., IBM Deep Blue)
2. **Limited Memory** — Can use past data for short-term decisions (e.g., self-driving cars)
3. **Theory of Mind** — Can understand emotions and beliefs (research stage)
4. **Self-Aware** — Has consciousness and self-awareness (theoretical)

## AI vs Machine Learning vs Deep Learning

```
┌─────────────────────────────────────────┐
│           Artificial Intelligence        │
│  ┌───────────────────────────────────┐  │
│  │        Machine Learning            │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │       Deep Learning          │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │   Generative AI       │  │  │  │
│  │  │  │  ┌─────────────────┐  │  │  │  │
│  │  │  │  │   Agentic AI    │  │  │  │  │
│  │  │  │  └─────────────────┘  │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

- **AI**: The broadest category — any technique that enables machines to mimic human intelligence
- **ML**: A subset of AI that learns patterns from data without explicit programming
- **DL**: A subset of ML using neural networks with many layers
- **GenAI**: A subset of DL that generates new content (text, images, code)
- **Agentic AI**: AI systems that act autonomously, using tools, memory, and planning

## Key AI Paradigms

### Symbolic AI (Good Old-Fashioned AI - GOFAI)
- Uses explicit rules and logic
- Knowledge represented as symbols and rules
- Example: Expert systems, logic programming
- Strength: Explainable, precise reasoning
- Weakness: Doesn't handle uncertainty or learn from data well

### Statistical/ML-Based AI
- Learns patterns from data
- Probabilistic reasoning
- Example: Neural networks, Bayesian methods
- Strength: Handles uncertainty, scales with data
- Weakness: Often a "black box", needs lots of data

### Hybrid AI (Modern Approach)
- Combines symbolic reasoning with statistical learning
- Neuro-symbolic AI
- Example: Modern AI agents that use LLMs + structured tools
- This is where **Agentic AI** shines — combining learning with structured reasoning

## The AI Technology Stack

```
┌─────────────────────────────────────┐
│         Applications                 │
│  Chatbots, Agents, Recommendation   │
├─────────────────────────────────────┤
│         Frameworks & Tools           │
│  LangChain, TensorFlow, PyTorch     │
├─────────────────────────────────────┤
│         Models & Algorithms          │
│  LLMs, CNNs, Transformers, RL       │
├─────────────────────────────────────┤
│         Data & Compute               │
│  Datasets, GPUs, Cloud, TPUs        │
├─────────────────────────────────────┤
│         Mathematics                  │
│  Linear Algebra, Calculus, Stats     │
└─────────────────────────────────────┘
```

## Connection to Agentic AI

Understanding AI fundamentals is crucial because:

1. **Agents are built ON TOP of AI** — every agent uses ML models for perception, reasoning, and action
2. **Agent decision-making** relies on the same optimization principles as classical ML
3. **Reinforcement Learning** is the direct ancestor of agent-based systems
4. **The evolution from narrow AI to agentic AI** represents the cutting edge of the field

## Summary

- AI is the broad field of creating intelligent machines
- Machine Learning is the most successful approach to AI today
- Deep Learning powers modern breakthroughs like LLMs
- Agentic AI represents the frontier — autonomous systems that plan, reason, and act
- Understanding the history and types of AI gives you the context to appreciate where Agentic AI fits
