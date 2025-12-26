from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.config import settings


pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# def hash_password(password: str) -> str:
#     # truncate password to 72 characters for bcrypt
#     truncated_password = password[:72]
#     return pwd_context.hash(truncated_password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     truncated_password = plain_password[:72]
#     return pwd_context.verify(truncated_password, hashed_password)


# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=expires_delta if expires_delta else settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


# from datetime import datetime, timedelta
# from jose import jwt
# from passlib.context import CryptContext
# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from app.config import settings

# pwd_context = CryptContext(schemes=["bcrypt"])
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# def hash_password(password: str):
#     return pwd_context.hash(password)

# def verify_password(password, hashed):
#     return pwd_context.verify(password, hashed)

# def create_access_token(data: dict):
#     expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     data.update({"exp": expire})
#     return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
