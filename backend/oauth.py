from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta

import jwt
from jwt import PyJWTError
from passlib.context import CryptContext

from .model import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "46936036427095cb76ed002fe7a168c24ee815003b5e5416916cd718f53a9b5d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        return username
    except PyJWTError:
        return None
