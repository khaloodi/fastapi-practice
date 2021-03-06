from db.hash import Hash
from sqlalchemy.orm.session import Session
from db.models import DbUser
from schemas import UserBase

# this file contains the functionality used to write to database
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all() #simply query the database session, grabbing and returning all users from DbUser table

def get_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id ==id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'

# def delete_user(db: Session, id: int, request: UserBase): -- first way
def delete_user(db: Session, id: int):
    # user = db.query(DbUser).filter(DbUser.id == id) -- first way
    user = db.query(DbUser).filter(DbUser.id == id).first()
    # user.delete() -- this line worked as well, first way
    db.delete(user)
    db.commit()
    return 'deleted'