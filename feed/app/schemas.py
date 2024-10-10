from pydantic import BaseModel


class User(BaseModel):
    login: str


class Message(BaseModel):
    id: int
    author_login: str
    text: str


class MessageCreate(BaseModel):
    text: str
