from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas
from database import get_db
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt




SECRET_KEY = "parassecretkey-createnoteinfastapi" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# password utitlities
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(plain_pasword):
    return pwd_context.hash(plain_pasword)


    
# token functions

def create_access_token(data:dict,expires_delta:Optional[timedelta]=None):
    payload=data.copy()
    
    if expires_delta:
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload.update({"exp":expire})
    encoded_jwt=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt