from pydantic import BaseModel # type: ignore

class UserCreate(BaseModel):

    username: str
    email: str
    password: str

class UserLogin(BaseModel):

    username: str
    password: str