from pydantic import BaseModel,EmailStr,Field

class SignupSchema(BaseModel):
    name:str=Field(
        min_length=2,
        max_length=100
    )
    organization_name:str=Field(
        min_length=2,
        max_length=100
    )
    username:str=Field(
        min_length=3,
        max_length=50
    )
    email:EmailStr
    password:str=Field(
        min_length=8,
        max_length=128
    )

class SigninSchema(BaseModel):
    email:EmailStr
    password:str=Field(
        min_length=8,
        max_length=128
    )

class TokenResponseSchema(BaseModel):
    access_token:str
    token_type:str="bearer"