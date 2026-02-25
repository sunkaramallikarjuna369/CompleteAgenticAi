# Fine-Tuning LLMs

## When to Fine-Tune vs RAG
| Scenario | Use RAG | Use Fine-Tuning |
|----------|---------|----------------|
| Domain knowledge | Yes | Maybe |
| Output format/style | No | Yes |
| Specific behavior | No | Yes |
| Frequently updated data | Yes | No |

## Fine-Tuning Methods
### Full Fine-Tuning
Update all parameters. Expensive, needs lots of data.

### LoRA (Low-Rank Adaptation)
Add small trainable matrices to frozen model. 10-100x fewer parameters.

### QLoRA
LoRA + 4-bit quantization. Fine-tune 65B models on single GPU.

### PEFT (Parameter-Efficient Fine-Tuning)
Umbrella term: LoRA, prefix tuning, adapters.

## Instruction Tuning
Fine-tune on instruction-response pairs to improve instruction following.

## RLHF (Reinforcement Learning from Human Feedback)
Align model outputs with human preferences using reward models.

## For Agentic AI
- Fine-tuning creates specialized agents
- LoRA/QLoRA make it affordable
- RLHF aligns agents with desired behavior