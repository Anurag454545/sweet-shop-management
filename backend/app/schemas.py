from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class SweetCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int
    
class SweetCreate(BaseModel):
    name: str
    price: int
    quantity: int
   
