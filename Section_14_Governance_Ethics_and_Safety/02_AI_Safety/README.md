# AI Safety

## Key Concepts
### Alignment
Ensuring AI systems do what we intend, not just what we literally say.

### Guardrails
Automatic safety checks on inputs and outputs:
- Content filtering (toxicity, PII, harmful content)
- Action validation (prevent destructive operations)
- Output validation (factuality, format)
- Rate limiting

### Red Teaming
Adversarial testing to find vulnerabilities:
- Prompt injection attacks
- Jailbreak attempts
- Edge cases and failure modes
- Social engineering scenarios

## Safety Frameworks
- NeMo Guardrails (NVIDIA)
- Guardrails AI
- Rebuff (prompt injection detection)
- LLM Guard

## For Agentic AI
- Agents with tool access are HIGH RISK
- Safety is the #1 concern for enterprise deployment
- Defense-in-depth: multiple layers of safety checks