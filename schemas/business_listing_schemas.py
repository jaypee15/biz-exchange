from pydantic import BaseModel

from business_schemas import Business

class BusinessListingBase(BaseModel):
    business: Business  
    price: float
    status: str  
    created_at: str
    updated_at: str

class BusinessListingCreate(BusinessListingBase):
    pass 

class BusinessListing(BusinessListingBase):
    id: int

    class Config:
        orm_mode = True