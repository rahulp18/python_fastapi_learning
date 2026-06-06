from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from sqlalchemy import select
from app.models.user import User
from app.schemas.auth_schema import SignupSchema
class UserRepository:
    
    @staticmethod
    async def get_by_email(db:AsyncSession,email:str)->User|None:
        statement=select(User).where(
            User.email==email
        )
        result=await db.execute(statement)

        return result.scalar_one_or_none()
    @staticmethod
    async def get_by_username(db:AsyncSession,username:str)->User|None:
        statement=select(User).where(
            User.username==username
        )
        result=await db.execute(statement)
        return result.scalar_one_or_none()
    @staticmethod
    async def create(db:AsyncSession,data:SignupSchema,hashed_password:str)->User:
        user=User(
            name=data.name,
            username=data.username,
            email=data.email,
            password=hashed_password
        )
        db.add(user)
        await db.flush()
        await db.refresh(user)
        return user
