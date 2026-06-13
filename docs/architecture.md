# Architecture Documentation

## Project Overview

This project demonstrates a cloud-native CI/CD pipeline and test automation framework for a Python FastAPI microservice. It includes automated testing, code quality checks, Docker containerization, Kubernetes deployment, GitHub Actions CI/CD workflows, Docker smoke testing, and container image publishing to GitHub Container Registry.

The goal of this project is to simulate a real-world engineering workflow where code changes are automatically validated before deployment.

## High-Level Architecture

```text
Developer
   |
   | git push / pull request
   v
GitHub Repository
   |
   v
GitHub Actions CI Pipeline
   |
   |-- Install dependencies
   |-- Run Ruff code quality checks
   |-- Validate Kubernetes manifests
   |-- Run Pytest API tests
   |-- Generate coverage reports
   |-- Enforce coverage threshold
   |-- Build Docker image
   |-- Run container smoke tests
   |-- Publish image to GitHub Container Registry
   v
GitHub Container Registry
   |
   v
Kubernetes Deployment
   |
   v
FastAPI Microservice
```

## Application Layer

The application is built using FastAPI and exposes service-monitoring endpoints.

Main endpoints:

| Method | Endpoint                 | Purpose                           |
| ------ | ------------------------ | --------------------------------- |
| GET    | `/`                      | Returns root API message          |
| GET    | `/health`                | Returns health status of the API  |
| GET    | `/services`              | Returns all service statuses      |
| GET    | `/services/{service_id}` | Returns a specific service status |

The `/health` endpoint is also used by Kubernetes readiness and liveness probes.

## Test Automation Layer

The test framework uses Pytest and FastAPI TestClient.

Testing includes:

* Root endpoint validation
* Health endpoint validation
* Service listing validation
* Individual service lookup validation
* Error handling validation for missing services

A reusable Pytest fixture is defined in `tests/conftest.py` so all test files can use the same FastAPI test client.

Coverage reporting is enabled using `pytest-cov`.

The project enforces a minimum coverage threshold of 80%. If test coverage drops below this threshold, the CI pipeline fails automatically.

## Code Quality Layer

Ruff is used for code quality checks, linting, and formatting.

Pre-commit hooks are configured to run quality checks before code is committed. This helps catch issues earlier in the development process.

Pre-commit checks include:

* Ruff linting
* Ruff formatting
* YAML validation
* Trailing whitespace removal
* End-of-file fixing
* Large file checks

## Containerization Layer

The application is containerized using Docker.

The Dockerfile defines:

* Python base image
* Application working directory
* Dependency installation
* Application source copy
* FastAPI startup command using Uvicorn

Docker Compose is also included to simplify local container execution.

## Kubernetes Deployment Layer

Kubernetes manifests are stored in the `k8s/` directory.

The Kubernetes deployment includes:

* Two application replicas
* Container image from GitHub Container Registry
* Readiness probe using `/health`
* Liveness probe using `/health`

The Kubernetes service exposes the application using NodePort so it can be accessed locally.

## CI/CD Pipeline

The GitHub Actions pipeline runs automatically on pushes and pull requests.

Pipeline stages:

1. Checkout repository
2. Set up Python
3. Install dependencies
4. Run Ruff code quality checks
5. Validate Kubernetes YAML manifests
6. Run automated API tests
7. Generate test and coverage reports
8. Enforce coverage quality gate
9. Build Docker image
10. Run Docker container
11. Perform smoke tests against containerized API
12. Publish Docker image to GitHub Container Registry

## Docker Smoke Testing

The CI pipeline performs container-level smoke testing after building the Docker image.

Smoke tests verify that:

* The Docker image builds successfully
* The container starts successfully
* The `/health` endpoint responds correctly
* The main API endpoints are reachable

This ensures that the application works not only in local Python execution, but also inside a production-like container environment.

## Deployment Flow

```text
Code Change
   |
   v
Git Commit
   |
   v
Pre-commit Checks
   |
   v
Git Push
   |
   v
GitHub Actions CI
   |
   v
Tests + Lint + Coverage + Docker Build
   |
   v
Docker Smoke Test
   |
   v
Publish Image to GHCR
   |
   v
Kubernetes Deployment Uses Published Image
```

## Reliability Practices Used

This project includes several engineering practices used in production systems:

* Automated testing before deployment
* Code quality enforcement
* Test coverage threshold
* Docker-based environment consistency
* Kubernetes health checks
* CI/CD automation
* Container image publishing
* Smoke testing after image build
* Pre-commit validation before code reaches GitHub

## Interview Talking Points

I built a CI/CD and test automation framework around a Python FastAPI microservice. The project includes automated API tests using Pytest, code quality checks with Ruff, coverage reporting with a minimum threshold, Docker containerization, Kubernetes deployment manifests, and a GitHub Actions pipeline.

The CI pipeline validates every code change by running lint checks, Kubernetes manifest validation, automated tests, coverage checks, Docker image builds, and container smoke tests. On successful pushes to the main branch, the pipeline publishes the Docker image to GitHub Container Registry.

This project helped me understand how modern engineering teams automate testing, validation, containerization, and deployment workflows to reduce regression issues and improve release reliability.
