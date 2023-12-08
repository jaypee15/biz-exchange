from pydantic import BaseModel
from user_schemas import UserSchema
class BusinessBase(BaseModel):

    name: str
    description: str
    owner: UserSchema
    industry: str
    location: str

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True