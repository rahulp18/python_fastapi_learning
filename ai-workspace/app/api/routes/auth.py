from fastapi import APIRouter,Depends
from app.api.dependencies.auth import get_current_user
from app.schemas.auth import(
    LoginRequest,
    TokenResponse
)
from sqlalchemy.orm import Session
from app.schemas.user import(
    UserCreate,
    UserResponse
)
from app.api.dependencies.db import get_db
from app.services.auth_service import(
    signin_service,
    signup_service
)

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post('/signup',response_model=UserResponse,status_code=201)
async def signup(user:UserCreate,db:Session=Depends(get_db)):
    return signup_service(db,user)

@router.post('/signin',response_model=TokenResponse,)
async def signin(login_data:LoginRequest,db:Session=Depends(get_db)):
    return signin_service(
        db,
        email=login_data.email,
        password=login_data.password
    )
@router.get("/me",response_model=UserResponse)
async def get_authenticated_item(current_user=Depends(get_current_user)):
    return current_user
     
