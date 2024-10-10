from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session


from .dependencies import get_db, get_user_from_token
from .models import DbMessage
from .schemas import Message, MessageCreate, User
from .database import Base, engine

app = FastAPI()


@app.post("/feed")
def add_message(message: MessageCreate, db: Session = Depends(get_db), user: User = Depends(get_user_from_token)) -> Message:
    db_message = DbMessage(
        author_login=user.login,
        text=message.text
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message


@app.get("/feed")
def get_messages(db: Session = Depends(get_db)) -> List[Message]:
    return db.query(DbMessage).order_by(DbMessage.id.desc()).limit(10)


Base.metadata.create_all(bind=engine)
