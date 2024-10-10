import os
from fastapi import FastAPI
import jwt

from .schemas import UserCreds, UserLogin

app = FastAPI()

JWT_SECRET = os.environ['JWT_SECRET']


@app.post("/login")
def login(user: UserLogin) -> UserCreds:
    token = jwt.encode({'login': user.login}, JWT_SECRET, algorithm='HS256')

    return UserCreds(token=token)
