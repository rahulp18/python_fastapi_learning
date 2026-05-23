from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.user import UserResponse
from app.core.security import(
    create_access_token,
    hash_password,
    verify_password
)

from app.repositories.user_repository import (
    create_user,
    get_user_by_email
)
from app.schemas.user import UserCreate

def signup_service(db:Session,user:UserCreate):
    existing_user=get_user_by_email(db,user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    hashed_password=hash_password(user.password)

    new_user={
        "name":user.name,
        "email":user.email,
        "password":hashed_password
    }

    created_user=create_user(db,new_user)
    return  {
         "id": created_user.id,
        "name": created_user.name,
        "email": created_user.email,
    }
def signin_service(
        db:Session,
        email:str,
        password:str
):
    user=get_user_by_email(db,email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    is_valid_password=verify_password(password,user.password)

    if not is_valid_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token=create_access_token({
        "sub":user.email
    })
    return {
        "access_token":access_token,
        "token_type":"Bearer"
    }