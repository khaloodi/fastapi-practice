from typing import List

from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

#use fastAPI to expose database creation to our API
router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create user
@router.post('/', response_model = UserDisplay) #system converts the model into data that can be displayed for us b/c of class Config in UserDisplay schema
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read all users
@router.get('/', response_model = List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read one user
@router.get('/{id}', response_model = UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# Update user
@router.post('/{id}/update')#createing endpoint to update user with specific id
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)

# Delete user