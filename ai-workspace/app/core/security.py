import jwt
import hashlib
from datetime import datetime,timedelta,timezone
from pwdlib import PasswordHash
from jwt.exceptions import InvalidTokenError
from app.core.config import settings

password_hash=PasswordHash.recommended()

def hash_password(password:str)->str:
    return password_hash.hash(password)

def verify_password(plain_password:str,hashed_password:str)->bool:
    return password_hash.verify(plain_password,hashed_password)

def create_access_token(data:dict)->str:
    to_encode=data.copy()

    expire=datetime.now(timezone.utc)+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp":expire,
        "type":"access"
    })

    encoded_jwt=jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt

def decode_access_token(token:str)->str|None:
    try:
        payload=jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload
    except InvalidTokenError:
        return None

def create_refresh_token(data:dict)->str:
    to_encode=data.copy()

    expire=datetime.now(timezone.utc)+timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    to_encode.update({
        "exp":expire,
        "type":"refresh"
    })

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def hash_token(token:str)->str:
    return hashlib.sha256(token.encode()).hexdigest()