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

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None