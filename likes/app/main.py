from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session


from .dependencies import get_db, get_user_from_token
from .models import DbLike
from .schemas import MessageLikes, ToggleLike, User
from .database import Base, engine

app = FastAPI()


@app.post("/likes")
def toggle_like(message: ToggleLike, db: Session = Depends(get_db), user: User = Depends(get_user_from_token)) -> MessageLikes:
    like = db.query(DbLike).where(
        DbLike.message_id == message.message_id,
        DbLike.user_login == user.login
    ).first()

    if like is None:
        db_like = DbLike(
            message_id=message.message_id,
            user_login=user.login
        )
        db.add(db_like)
        db.commit()
    else:
        db.delete(like)
        db.commit()

    likes_count = db.query(DbLike).where(
        DbLike.message_id == message.message_id).count()

    return MessageLikes(count=likes_count)


@app.get("/likes")
def get_likes(message_id: str, db: Session = Depends(get_db)) -> MessageLikes:
    likes_count = db.query(DbLike).where(
        DbLike.message_id == message_id).count()

    return MessageLikes(count=likes_count)


Base.metadata.create_all(bind=engine)
