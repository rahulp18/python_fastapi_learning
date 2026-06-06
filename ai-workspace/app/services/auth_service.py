from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import SignupSchema,SigninSchema
from app.core.security import hash_password,verify_password,create_access_token
from app.services.organization_service import OrganizationService
 
class AuthService: 
    @staticmethod
    async def signup(db:AsyncSession,data:SignupSchema):
        try:
            # CHECK EMAIL EXISTS
            existing_email=await UserRepository.get_by_email(db,data.email)

            if existing_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )
            # CHECK USERNAME EXISTS
            existing_username=await UserRepository.get_by_username(db,data.username)
            if existing_username:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already exists"
                )
            hashed_password=hash_password(data.password)
            # CREATE USER
            user=await UserRepository.create(
                db,
                data,
                hashed_password
            )
            # organization and workspace create
            await OrganizationService.create_org_with_workspace(
                db=db,
                user=user,
                org_name=data.organization_name
            )
 
            await db.commit()
            return user
        except:
            await db.rollback()
            raise
    
    @staticmethod
    async def signin(db:AsyncSession,data:SigninSchema):
        user=await UserRepository.get_by_email(db,data.email)
        
        if not user or not verify_password(data.password,user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
  
        access_token=create_access_token(
            {
                "sub":str(user.id),
                "email":user.email
            }
        )

        return {
            "access_token":access_token,
            "token_type":"Bearer"
        }

