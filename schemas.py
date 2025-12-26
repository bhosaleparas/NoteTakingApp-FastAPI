from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional,List


# userschemas
class UserBase(BaseModel):
    email:EmailStr
    username:str
    ful_name:Optional[str] =None

class UserCreate(UserBase):
    password:str
    

class UserUpdate(BaseModel):
    email:Optional[EmailStr]=None
    username:Optional[str]=None
    ful_name:Optional[str]=None
    password:Optional[str]=None

class User(UserBase):
    id:int
    created_at:datetime

    class Config:
        from_attributes=True


# Note schema

class NoteBase(BaseModel):
    title:str
    content:Optional[str]=None
    
class NoteCreate(NoteBase):
    pass


class NoteBase(BaseModel):
    title:Optional[str]=None
    content:Optional[str]=None
    
class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class Note(NoteBase):
    id:int
    owner_id:int
    created_at:datetime
    updated_at:Optional[datetime]=None
    
    class Config:
        from_attributes=True



# Token Schema
