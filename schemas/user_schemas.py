from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserSchema(UserBase):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class UserCreate(UserSchema):
    password: str