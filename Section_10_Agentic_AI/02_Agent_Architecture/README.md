# Agent Architecture

## Core Components
```
┌─────────────────────────────────────┐
│           AGENT SYSTEM              │
│                                     │
│  ┌─────────┐  ┌──────────────────┐ │
│  │  LLM    │  │  System Prompt   │ │
│  │ (Brain) │  │  (Instructions)  │ │
│  └────┬────┘  └──────────────────┘ │
│       │                             │
│  ┌────┴────┐  ┌──────────────────┐ │
│  │ Planner │  │     Memory       │ │
│  └────┬────┘  │ (Short + Long)   │ │
│       │       └──────────────────┘ │
│  ┌────┴────┐                       │
│  │  Tools  │  ┌──────────────────┐ │
│  │ (APIs,  │  │   Guardrails     │ │
│  │  Code)  │  │   (Safety)       │ │
│  └─────────┘  └──────────────────┘ │
└─────────────────────────────────────┘
```

## Architecture Patterns
- **Single Agent**: One LLM with tools
- **Router Agent**: Routes to specialized sub-agents
- **Pipeline Agent**: Sequential processing stages
- **Supervisor Agent**: Oversees worker agents
- **Swarm**: Decentralized agent collaboration

## For Architects
- Start with single agent, evolve to multi-agent as needed
- Always include guardrails and observability