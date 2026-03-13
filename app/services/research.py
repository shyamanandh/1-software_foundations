from app.models.company import CompanyProfile

# This is MOCK data for now
# Day 3 → this becomes a real LLM call
# The structure stays exactly the same

async def research_company(company_name: str) -> CompanyProfile:
    
    # Simulating what an LLM will return later
    mock_data = {
        "Anthropic": CompanyProfile(
            name="Anthropic",
            industry="AI Safety",
            headquarters="San Francisco, CA",
            description="AI safety company building reliable AI systems",
            tech_stack=["Python", "AWS", "PyTorch"]
        ),
        "Google": CompanyProfile(
            name="Google",
            industry="Technology",
            headquarters="Mountain View, CA",
            description="Global technology company focused on search and AI",
            tech_stack=["Python", "Go", "Kubernetes"]
        ),
    }

    # If company exists in mock data return it
    # If not → return a default profile
    return mock_data.get(company_name, CompanyProfile(
        name=company_name,
        industry="Unknown",
        headquarters="Unknown",
        description=f"{company_name} - research pending",
        tech_stack=[]
    ))
