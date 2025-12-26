from sqlalchemy.orm import Session
from sqlalchemy import and_
import models
import schemas
from auth import get_password_hash, verify_password


# User crud operation

def get_user(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id==user_id).first()

def get_user_email(db:Session,user_email:str):
    return  db.query(models.User).filter(models.User.email==user_email).first()

def get_user_by_username(db:Session,username:str):
    return  db.query(models.User).filter(models.User.username==username).first()

def get_users(db:Session,skip:int=0,limit:int=100):
    return db.query(models.User).all()


def create_user(db:Session,user:schemas.UserCreate):
    # check for  user
    user_email=get_user_email(db,user.email)
    if user_email:
        raise ValueError("email already exists")
    
    user_name=get_user_by_username(db,username=user.username)
    if user_name:
        raise ValueError("username already taken")

    # user not found create new user
    
    # hash password
    hash_password=get_password_hash(user.password)

    # create user
    db_user=models.User(
        email=user.email,
        username=user.username,
        ful_name=user.ful_name,
        hashed_password=hash_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    
    #finding user by username
    user = get_user_by_username(db, username)  
    
    #checking username is exits or not
    if not user:  
        return False
    
    if not verify_password(password, user.hashed_password):
        return False
    
    return user


# note crud operation

def get_note(db:Session,note_id:int, user_id:int):
    return db.query(models.Notes).filter(and_(models.Notes.id==note_id,models.Notes.owner_id==user_id)).first()


def get_notes(db:Session,user_id:int):
    return db.query(models.Notes).filter(models.Notes.owner_id==user_id).all()


def create_note(db:Session,note:schemas.NoteCreate,user_id:int):
    db_note=models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note



def update_note(db: Session, note_id: int, note_update: schemas.NoteUpdate, user_id: int):
    db_note = get_note(db, note_id, user_id)
    if not db_note:
        return None
    
    update_data = note_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_note, field, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int, user_id: int):
    db_note = get_note(db, note_id, user_id)
    if not db_note:
        return False
    
    db.delete(db_note)
    db.commit()
    return True



#search note by title or content 
def search_notes(db: Session, user_id: int, query: str):
    return db.query(models.Note).filter(
        and_(
            models.Note.owner_id == user_id,
            (models.Note.title.contains(query)) | (models.Note.content.contains(query))
        )
    ).all()