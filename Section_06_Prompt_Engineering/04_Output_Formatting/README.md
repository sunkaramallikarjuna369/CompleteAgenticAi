# Output Formatting

## Why Structured Output?
Agents need to produce machine-readable output for tool calls, API interactions, and downstream processing.

## Techniques
### JSON Mode
Force LLM to output valid JSON.

### Function Calling
LLM outputs structured tool calls:
```json
{"name": "search", "arguments": {"query": "weather NYC"}}
```

### Pydantic/Schema Validation
Define output schema, validate responses.

### Constrained Generation
Grammar-based decoding (Outlines, LMQL).

## For Agentic AI
- Function calling IS how agents use tools
- Structured output ensures reliable agent behavior
- JSON mode prevents parsing errors