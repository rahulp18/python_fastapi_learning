from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.permission import Permission

class PermissionRepository:

    @staticmethod
    async def get_all(db:AsyncSession):
        results=await db.execute(select(Permission))

        return results.scalars().all()
    
    @staticmethod
    async def get_by_key(db:AsyncSession,key:str):
        result=await db.execute(select(Permission).where(
            Permission.key==key
        ))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def create(db,key:str,description:str|None=None):
        permission=Permission(
            key=key,
            description=description
        )
        db.add(permission)
        await db.flush()
        return permission