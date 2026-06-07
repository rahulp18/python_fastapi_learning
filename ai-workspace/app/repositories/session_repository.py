from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime,timezone
from app.models import Session
from sqlalchemy import select
class SessionRepository:

    @staticmethod
    async def create(
        db:AsyncSession,
        user_id:str,
        refresh_token_hash:str,
        user_agent:str|None,
        ip_address:str|None,
        expires_at:datetime
                     ):
        session=Session(
            user_id=user_id,
            refresh_token_hash=refresh_token_hash,
            user_agent=user_agent,
            ip_address=ip_address,
            expires_at=expires_at
        )
        db.add(session)
        await db.flush()
        await db.refresh(session)
        return session
    @staticmethod
    async def get_active_by_user_id(db:AsyncSession,user_id:str):
        now=datetime.now(timezone.utc)
        result=await db.execute(
            select(Session).where(
                Session.user_id==user_id,
                Session.revoked_at.is_(None),
                Session.expires_at>now
            )
        )
        return result.scalars().all()
    @staticmethod
    async def get_session_by_id(db:AsyncSession,id:str):
        result=await db.execute(
            select(Session).where(
                Session.id==id
            )
        )
        return result.scalar_one_or_none()
