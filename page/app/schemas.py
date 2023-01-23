from pydantic import BaseModel

class UserBase(BaseModel):
    id: str

class User(UserBase):
    name: str
    password: str

    class Config:
        orm_mode = True

class Data(BaseModel):
    use : list
    weather : str