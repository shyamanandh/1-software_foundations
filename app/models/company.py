from pydantic import BaseModel
from typing import Optional

# What comes IN to your API
class CompanyRequest(BaseModel):
    company_name: str
    include_competitors: bool = False

# What a company profile looks like
class CompanyProfile(BaseModel):
    name: str
    industry: str
    headquarters: str
    description: str
    tech_stack: list[str] = []

# Every API response has same wrapper
class APIResponse(BaseModel):
    success: bool
    data: Optional[CompanyProfile] = None
    error: Optional[str] = None