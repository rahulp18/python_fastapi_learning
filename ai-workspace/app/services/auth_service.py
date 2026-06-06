from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import SignupSchema
from app.core.security import hash_password
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
        except Exception:
            await db.rollback()
            raise
