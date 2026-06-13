from fastapi import FastAPI, HTTPException

app = FastAPI(title="Service Status API")

services = {
    1: {"name": "auth-service", "status": "healthy"},
    2: {"name": "payment-service", "status": "healthy"},
    3: {"name": "notification-service", "status": "degraded"},
}


@app.get("/")
def root():
    return {"message": "CI/CD Test Automation Framework API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/services")
def get_services():
    return services


@app.get("/services/{service_id}")
def get_service(service_id: int):
    if service_id not in services:
        raise HTTPException(status_code=404, detail="Service not found")
    return services[service_id]