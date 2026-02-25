# Serverless AI

## Why Serverless for AI Agents?
- Pay only for actual usage
- Auto-scaling to zero
- No infrastructure management
- Fast deployment

## Serverless Options
| Service | Provider | Max Timeout | GPU? |
|---------|----------|-------------|------|
| Lambda | AWS | 15 min | No |
| Cloud Functions | GCP | 60 min | No |
| Azure Functions | Azure | Unlimited | No |
| Modal | Independent | Unlimited | Yes |
| Beam | Independent | Unlimited | Yes |

## Serverless Agent Patterns
- API Gateway + Lambda for simple agents
- Step Functions for multi-step workflows
- Event-driven processing with SQS/SNS

## Limitations
- Cold starts (1-5 seconds)
- Timeout limits
- No GPU for Lambda/Cloud Functions
- Limited memory

## For Architects
- Serverless is ideal for low-to-medium volume agent workloads
- Use containers for high-volume or GPU-dependent workloads