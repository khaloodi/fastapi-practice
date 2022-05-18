from sqlalchemy import Column, Integer, String

from db.database import Base

# this file contains our database tables
class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String) #password is automatically hashed