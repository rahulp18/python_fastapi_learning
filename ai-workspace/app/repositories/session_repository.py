from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from app.models import Session
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
        
