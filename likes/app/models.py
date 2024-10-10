from sqlalchemy import Column, Integer, String, UniqueConstraint

from .database import Base


class DbLike(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_login = Column(String)
    message_id = Column(Integer)

    __table_args__ = (
        UniqueConstraint('user_login', 'message_id', name='_uc'),
    )
