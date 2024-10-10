from pydantic import BaseModel


class User(BaseModel):
    login: str


class MessageLikes(BaseModel):
    count: int


class ToggleLike(BaseModel):
    message_id: int
