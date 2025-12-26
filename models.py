from sqlalchemy import Column, Integer, String,  Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,index=True,nullable=False)
    username=Column(String,nullable=False,unique=True,index=True)
    ful_name=Column(String)
    hashed_password=Column(String,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    
    # relationships with notes
    notes=relationship("Notes",back_populates='owner',cascade="all, delete-orphan")
    

class Notes(Base):
    __tablename__="notes"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String, index=True,nullable=False)
    contenet=Column(Text)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),onupdate=func.now())
    owner_id=Column(Integer,ForeignKey('users.id'),nullable=False)

    # relationship
    owner=relationship("User",back_populates="notes")