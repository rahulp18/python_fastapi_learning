from fastapi import APIRouter,Depends
# from app.api.dependencies.auth import get_current_user
 
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schema import UserResponseSchema
from app.schemas.auth_schema import SignupSchema
from app.api.dependencies.db import get_db
from app.services.auth_service import AuthService
router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post('/signup',response_model=UserResponseSchema,status_code=201)
async def signup(user:SignupSchema,db:AsyncSession=Depends(get_db)):
    return await AuthService.signup(db,user)

# @router.post('/signin',response_model=TokenResponseSchema,)
# async def signin(login_data:SigninSchema,db:Session=Depends(get_db)):
#     return AuthService.signin(
#         db,
#         email=login_data.email,
#         password=login_data.password
#     )
# @router.get("/me",response_model=UserResponseSchema)
# async def get_authenticated_item(current_user=Depends(get_current_user)):
#     return current_user
     
