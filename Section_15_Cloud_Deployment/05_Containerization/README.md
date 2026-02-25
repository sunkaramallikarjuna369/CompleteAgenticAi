# Containerization for AI

## Docker for AI
### Agent Service Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Kubernetes for AI
### Key Components
- **Deployments**: Agent service instances
- **Services**: Internal load balancing
- **Ingress**: External traffic routing
- **ConfigMaps/Secrets**: Configuration and credentials
- **HPAs**: Auto-scaling based on metrics
- **GPU Scheduling**: For self-hosted model inference

## Container Best Practices for AI
- Use multi-stage builds to minimize image size
- Pin dependency versions
- Never store secrets in images
- Use health checks for readiness/liveness
- Set resource limits (CPU, memory, GPU)

## For Architects
- Kubernetes is the standard for production AI workloads
- Use managed K8s (EKS, AKS, GKE) to reduce operational burden