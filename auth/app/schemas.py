from pydantic import BaseModel


class UserLogin(BaseModel):
    login: str


class UserCreds(BaseModel):
    token: str
