from fastapi import APIRouter, HTTPException
from app.models.company import CompanyRequest, APIResponse
from app.services.research import research_company

router = APIRouter(prefix="/v1/company", tags=["Company Research"])

# Health check for this router
@router.get("/health")
async def health():
    return {"status": "healthy", "service": "company-research"}

# Main endpoint
# POST /v1/company/research
# Send company name → get back company profile
@router.post("/research", response_model=APIResponse)
async def research_company_endpoint(request: CompanyRequest):
    try:
        # Call the service (brain)
        profile = await research_company(request.company_name)
        
        # Return structured response
        return APIResponse(
            success=True,
            data=profile
        )
    
    except Exception as e:
        # Something went wrong → return clean error
        raise HTTPException(status_code=500, detail=str(e))
