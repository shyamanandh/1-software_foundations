from fastapi import FastAPI
from app.routers import company

# Create the app
app = FastAPI(
    title="GTM Intelligence API",
    description="Company research for sales teams",
    version="0.1.0"
)

# Connect the router
# All routes from routers/company.py are now active
app.include_router(company.router)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "GTM Intelligence API is running",
        "docs": "visit /docs to see all endpoints",
        "version": "0.1.0"
    }
