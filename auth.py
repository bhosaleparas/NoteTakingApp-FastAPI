from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas
from database import get_db
from fastapi.security import OAuth2PasswordBearer



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# password utitlities
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_hashed_password(plain_pasword):
    return pwd_context.hash(plain_pasword)


    
