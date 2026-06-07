from fastapi import Request,HTTPException,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime,timezone
from app.core.security import decode_access_token
from app.repositories.user_repository import UserRepository
from app.repositories.session_repository import SessionRepository
from app.api.dependencies.db import get_db


async def get_current_user(
        request:Request,
        db:AsyncSession=Depends(get_db)
):
    auth_header=request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(401,"Missing token")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(401, "Invalid auth header")
    token = auth_header.split(" ")[1].strip()
    payload=decode_access_token(token)

    if not payload:
        raise HTTPException(401,"Invalid token")

    user_id=payload.get("sub")
    session_id=payload.get("session_id")

    user=await UserRepository.get_user_by_id(db,user_id)

    if not user:
        raise HTTPException(401,"User not found")
    # 2. OPTIONAL BUT IMPORTANT: verify session exists
    session = await SessionRepository.get_session_by_id(db, session_id)

    if not session or session.revoked_at is not None:
        raise HTTPException(status_code=401, detail="Session invalid")

    if session.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=401, detail="Session expired")
    
    request.state.user=user
    request.state.session_id=session_id

    return user
