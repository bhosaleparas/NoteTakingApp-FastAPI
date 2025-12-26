from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
import crud
import models
import schemas
import auth
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Note Taking API", version="1.0.0")

@app.get('/')
def root():
    return {"Message":"Welcome to note taking app"}


@app.post('/signup',response_model=schemas.User,status_code=status.HTTP_201_CREATED)
def signup(user:schemas.UserCreate, db:Session=Depends(get_db)):
    try:
        db_user=crud.create_user(db,user)
        return db_user
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
