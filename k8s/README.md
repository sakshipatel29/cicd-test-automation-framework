# Kubernetes Deployment

This folder contains Kubernetes manifests for deploying the FastAPI service.

## Files

- `deployment.yaml`: Creates two replicas of the FastAPI API service.
- `service.yaml`: Exposes the API using a NodePort service.

## Apply manifests

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml