from db.hash import Hash
from sqlalchemy.orm.session import Session
from db.models import DbUser
from schemas import UserBase

#
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