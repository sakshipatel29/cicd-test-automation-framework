cat > README.md <<'EOF'
# CI/CD Pipeline & Test Automation Framework

![CI Pipeline](https://github.com/sakshipatel29/cicd-test-automation-framework/actions/workflows/ci.yml/badge.svg)

A cloud-native CI/CD and test automation project built for a Python FastAPI microservice.  
The project demonstrates automated testing, Docker containerization, Kubernetes deployment, and GitHub Actions-based continuous integration.

## Project Overview

This project simulates a real-world microservices deployment workflow. It includes a FastAPI service with multiple endpoints, automated API tests, Docker support, Kubernetes manifests, and a GitHub Actions CI pipeline that validates code changes before deployment.

## Tech Stack

- Python
- FastAPI
- Pytest
- Docker
- Kubernetes
- GitHub Actions
- Uvicorn

## Features

- Built a FastAPI-based microservice for service health and status monitoring.
- Implemented automated API tests using Pytest and FastAPI TestClient.
- Containerized the application using Docker.
- Added Kubernetes deployment and service manifests.
- Configured GitHub Actions to run tests and validate Docker builds on every push and pull request.
- Created a reusable structure for API validation and CI/CD automation.

## CI/CD Capabilities

This project includes a production-style CI/CD workflow using GitHub Actions.

The pipeline performs:

- Dependency installation
- Code quality checks using Ruff
- Automated API testing using Pytest
- Test coverage reporting
- Coverage quality gate enforcement
- Docker image build validation
- Docker image publishing to GitHub Container Registry

The CI pipeline fails automatically if tests fail, linting fails, Docker build fails, or code coverage drops below the required threshold.

## Project Structure

```text
cicd-test-automation-framework/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md

## Docker Compose Usage

Run the application using Docker Compose:

```bash
docker compose up --build

---

## Step 16D: Add GHCR image section

Add this after the **GitHub Actions CI Pipeline** section:

```markdown
## Container Registry

The Docker image is automatically published to GitHub Container Registry when changes are pushed to the `main` branch.

Image:

```text
ghcr.io/sakshipatel29/cicd-test-automation-framework:latest