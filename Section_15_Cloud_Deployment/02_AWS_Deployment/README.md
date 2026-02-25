# AWS Deployment for AI Agents

## Key AWS Services

### Amazon Bedrock
Managed access to foundation models (Claude, Llama, Titan).
- Serverless, pay-per-token
- Knowledge bases (RAG)
- Agents (built-in agent framework)
- Guardrails

### Amazon SageMaker
Full ML lifecycle management.
- Model training and fine-tuning
- Model hosting (real-time + batch)
- SageMaker JumpStart (pre-trained models)

### AWS Lambda
Serverless compute for agent tools and event processing.

### Amazon ECS/EKS
Container orchestration for agent services.

### Vector Databases on AWS
- Amazon OpenSearch (vector search)
- Amazon Neptune (graph database)
- Pinecone/Qdrant on EC2 or ECS

## Example Architecture
```
API Gateway -> Lambda/ECS (Agent) -> Bedrock (LLM)
                    |                     |
              OpenSearch (RAG)    S3 (Documents)
                    |
              DynamoDB (State)    CloudWatch (Monitoring)
```

## Cost Optimization
- Use Bedrock for serverless inference
- Spot instances for non-critical workloads
- Reserved capacity for predictable loads
- S3 intelligent tiering for document storage

## For Architects
- AWS Bedrock provides the fastest path to production agents
- Combine Bedrock + OpenSearch + Lambda for serverless agents