from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.repositories.user_repository import get_user_by_email
from app.api.dependencies.db import get_db
oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl='/auth/signin'
)

async def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    payload=decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    email=payload.get("sub")

    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="In Valid token"
        )
    user=get_user_by_email(db,email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user
 

