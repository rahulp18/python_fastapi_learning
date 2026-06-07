from fastapi import HTTPException,status,Request
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime,timezone,timedelta
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import SignupSchema,SigninSchema
from app.core.security import (hash_password,
                               verify_password,
                               create_access_token,
                               create_refresh_token,
                               hash_token,
                               decode_access_token
                               )
from app.services.organization_service import OrganizationService
from app.repositories.session_repository import SessionRepository
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
    async def signin(db:AsyncSession,data:SigninSchema,request:Request):
        user=await UserRepository.get_by_email(db,data.email)
        
        if not user or not verify_password(data.password,user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        ip_address=request.headers.get('x-forwarded-for') or request.client.host
        user_agent=request.headers.get("user-agent")

        expires_at=datetime.now(timezone.utc)+timedelta(days=30)

        refresh_token=create_refresh_token(
            {
                "sub":str(user.id)
            }
        )
        # store session in db 
        session=await SessionRepository.create(
            db=db,
            user_id=user.id,
            refresh_token_hash=hash_token(refresh_token),
            user_agent=user_agent,
            ip_address=ip_address,
            expires_at=expires_at
        )
        await db.commit()
        access_token=create_access_token(
            {
                "sub":str(user.id),
                "session_id":str(session.id),
                "email":user.email,
                "type":"access"
            }
        )

        return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "token_type":"Bearer"
        }

    @staticmethod
    async def refresh_token(db:AsyncSession,refresh_token:str):
        payload=decode_access_token(refresh_token)

        if not payload or payload.get("type") !="refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
        user_id=payload['sub']

        sessions=await SessionRepository.get_active_by_user_id(db,user_id)
        if not sessions:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Sessions not found")
        
        session=None
        for s in sessions:
            if s.refresh_token_hash==hash_token(refresh_token):
                session=s
                break
        if not session:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token mismatched"
            )
 
        if session.expires_at <datetime.now(timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session expired"
            )
        new_refresh_token=create_refresh_token(
            {
              "sub":user_id
            }
        )

        session.refresh_token_hash=hash_token(new_refresh_token)
        session.last_used_at=datetime.now(timezone.utc)

        # create new access token
        new_access_token=create_access_token(
            {
                "sub":user_id,
                "session_id":session.id,
                "type":"access"
            }
        )
        await db.commit()

        return {
             "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "token_type": "Bearer"
        }


