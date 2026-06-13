install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	python -m uvicorn app.main:app --reload

test:
	python -m pytest

lint:
	ruff check .

format:
	ruff check . --fix

docker-build:
	docker build -t cicd-test-automation-api .

docker-run:
	docker run -p 8000:8000 cicd-test-automation-api

compose-up:
	docker compose up --build

compose-down:
	docker compose down

k8s-apply:
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml

k8s-delete:
	kubectl delete -f k8s/service.yaml
	kubectl delete -f k8s/deployment.yaml
