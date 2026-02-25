# Prompt Security

## Threats
### Prompt Injection
Attacker inserts malicious instructions into user input.

### Jailbreaking
Bypass safety guardrails through creative prompting.

### Data Exfiltration
Trick the model into revealing system prompts or training data.

## Defenses
- Input sanitization and validation
- Output filtering and monitoring
- System prompt protection
- Content safety classifiers
- Rate limiting and anomaly detection
- Guardrail frameworks (NeMo Guardrails, Guardrails AI)

## For Agentic AI
- Agents with tool access are HIGH RISK targets
- An injected prompt could cause agents to execute harmful actions
- Defense-in-depth is essential: validate inputs, outputs, AND actions