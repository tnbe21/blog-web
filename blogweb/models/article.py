from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    DateTime
    )

from . import Base


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    author = Column(String)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)


Index('article_index', Article.id, unique=True, mysql_length=255)
