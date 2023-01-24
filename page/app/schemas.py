from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    name: str
    password: str

    class Config:
        orm_mode = True

class Data(BaseModel):
    use : list
    weather : str
    datetime : str