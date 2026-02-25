# GCP Deployment for AI Agents

## Key GCP Services

### Vertex AI
Google's unified ML platform.
- Model Garden (access to Gemini, PaLM, open models)
- Agent Builder (low-code agent creation)
- Vector Search (managed vector database)
- Model training and fine-tuning

### Cloud Run
Serverless containers for agent services.

### Cloud Functions
Serverless compute for tools and events.

### AlloyDB / Cloud SQL
Managed databases with vector extension support.

### BigQuery
Data warehouse with vector search and ML capabilities.

## Example Architecture
```
Cloud Load Balancer -> Cloud Run (Agent) -> Vertex AI (Gemini)
                            |                     |
                      Vector Search (RAG)   Cloud Storage (Docs)
                            |
                      Firestore (State)     Cloud Monitoring
```

## For Architects
- Vertex AI provides the most integrated ML platform
- Gemini offers competitive performance with long context
- Best for organizations using Google Workspace