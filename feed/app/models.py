from sqlalchemy import Column, Integer, String

from .database import Base


class DbMessage(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    author_login = Column(String)
    text = Column(String)
