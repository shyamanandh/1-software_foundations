# 01 — Software Foundations

## What This Is
A production-grade FastAPI microservice — the base layer 
of the GTM Intelligence Platform.

## What It Does
Accepts a company name → returns structured company profile

## API Endpoints
- POST /v1/company/research → research a company
- GET  /v1/company/health   → service health check

## Why These Choices
- **FastAPI** → async support for concurrent LLM calls
- **Pydantic** → validates and structures all data
- **Docker** → runs identically everywhere
- **Layered architecture** → router/service/model separation

## How To Run
```bash
# Without Docker
uvicorn app.main:app --reload

# With Docker
docker compose up
```

## How This Connects To GTM Platform
This is the API skeleton.
Component 02 replaces mock data with real LLM calls.
Every other component builds on top of this.

## What I Learned
- Async functions handle multiple requests simultaneously
- Pydantic validates data before it reaches business logic
- Separating routers/services/models makes code maintainable
- Docker packages entire environment not just code