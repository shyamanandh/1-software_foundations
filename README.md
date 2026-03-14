# 1-software_foundations

# Component 01 — Company Research API

## Overview

This component is the **first building block of the GTM (Go-To-Market) system**.

Its purpose is to create a **simple API service that receives a company name and returns structured company information**.

At this stage, the system returns **mock / placeholder data**.
In later components this will be replaced with **real data sources, AI models, and research pipelines**.

This component mainly establishes the **API infrastructure** that future components will plug into.

---

# Core Outcome

After completing this component you will have:

• A running **FastAPI server**
• An API endpoint that accepts **company name input**
• A response that returns **structured company profile data**
• A clean **data validation layer using Pydantic models**
• A basic **research service function** (mock implementation)

---

# System Architecture

```
User / Client
     │
     ▼
HTTP Request
     │
     ▼
FastAPI Router
     │
     ▼
Request Validation (Pydantic Model)
     │
     ▼
Research Service Function
(research_company)
     │
     ▼
Mock Company Data
     │
     ▼
Response Model Formatting
     │
     ▼
API Response returned to User
```

---

# End-to-End Flow Diagram

```
Client
 (Postman / Browser / Frontend)
        │
        │ 1️⃣ Send request
        ▼
POST /company-research
        │
        ▼
FastAPI Endpoint
(api/routes/company.py)
        │
        │ receives request
        ▼
CompanyRequest Model
(models/request_models.py)

Example Request:
{
 "company_name": "Tesla"
}

        │
        │ validation
        ▼
Research Service
(services/research_service.py)

profile = await research_company(request.company_name)

        │
        │ generate mock company data
        ▼
CompanyProfile Model
(models/response_models.py)

{
 "name": "Tesla",
 "industry": "Electric Vehicles",
 "headquarters": "Austin, Texas"
}

        │
        ▼
FastAPI Response
        │
        ▼
Client receives structured company data
```

---

# Folder Structure

```
component_01_company_research

│
├── main.py
│
├── api
│   └── routes
│       └── company.py
│
├── models
│   ├── request_models.py
│   └── response_models.py
│
├── services
│   └── research_service.py
│
└── README.md
```

---

# Component Responsibilities

### 1. API Layer

Handles HTTP requests and responses.

File:

```
api/routes/company.py
```

Responsibilities

• Define API endpoint
• Accept request body
• Call research service
• Return response model

---

### 2. Request Model

File:

```
models/request_models.py
```

Purpose

Defines **what data the API expects from the client**.

Example:

```python
class CompanyRequest(BaseModel):
    company_name: str
    include_competitors: bool = False
```

---

### 3. Response Model

File:

```
models/response_models.py
```

Purpose

Defines **what data the API returns to the user**.

Example:

```python
class CompanyProfile(BaseModel):
    name: str
    industry: str
    headquarters: str
```

---

### 4. Research Service

File:

```
services/research_service.py
```

Purpose

Contains the **business logic for retrieving company data**.

Currently:

• Returns **mock data**

Later components will replace this with:

• Web scraping
• Knowledge base lookup
• LLM research pipelines

Example:

```python
async def research_company(company_name: str):
```

---

# Example API Request

```
POST /company-research
```

Body:

```
{
 "company_name": "Tesla"
}
```

---

# Example API Response

```
{
 "name": "Tesla",
 "industry": "Electric Vehicles",
 "headquarters": "Austin, Texas"
}
```

---

# Running the Server

Install dependencies

```
pip install fastapi uvicorn pydantic python-dotenv
```

Start the API server

```
uvicorn main:app --reload
```

Server will start at

```
http://127.0.0.1:8000
```

API documentation available at

```
http://127.0.0.1:8000/docs
```

---

# What This Component Establishes

This component builds the **foundation of the GTM system**.

It sets up:

• API infrastructure
• Data validation layer
• Business logic layer
• Structured response format

Future components will expand this system with:

• real research data
• AI powered analysis
• competitor discovery
• market insights generation

---

# Key Concept Learned

This component demonstrates the **standard backend data pipeline**.

```
Input → Validation → Processing → Response
```

Where

```
Input      → Company name
Validation → Pydantic models
Processing → research_company()
Response   → CompanyProfile
```

---

# Next Component

The next component will replace **mock research data with real company intelligence sources**.

Possible integrations:

• Web search APIs
• Company databases
• AI summarization pipelines

This will transform the API from a **mock research system into a real company intelligence engine**.
