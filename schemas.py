from pydantic import BaseModel

# type of data we receive from the user
class UserBase(BaseModel): #data from user: UserBase
    username: str
    email: str
    password: str

#define a type of data that gets sent back to the user
class UserDisplay(BaseModel): #data to user: UserDisplay
    username: str
    email: str
    class Config():
        #this allows system to return database data in the format specified above
        orm_mode = True