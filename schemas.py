from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

#define a type that gets sent back to the user
class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        #this allows system to return database data in the format specified above
        orm_mode = True