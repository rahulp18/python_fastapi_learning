from datetime import datetime,timedelta,timezone
import jwt
from pwdlib import PasswordHash
from jwt.exceptions import InvalidTokenError
from app.core.config import settings
import random
import string
import re
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
        type:"access"
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

def slugify(text:str)->str:
    text=text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)

    return text

async def generate_uniq_slug(name:str,slug_exists)->str:
    base_slug=slugify(name)
    alphabet=string.ascii_letters+string.digits

    while True:
        suffix="".join(random.choices(alphabet,k=5))

        slug=f"{base_slug}-{suffix}"

        if not await slug_exists(slug):
            return slug
