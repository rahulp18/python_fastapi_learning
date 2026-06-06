from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserResponseSchema(BaseModel):
    id:str
    name:str
    email:EmailStr
    username:str
    created_at:datetime
    updated_at:datetime
    
    model_config={
        "from_attributes":True
    }