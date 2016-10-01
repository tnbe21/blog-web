import time
from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String
)

from . import Base, DBSession


class ArticleTag(Base):
    __tablename__ = 'article_tag'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    article_id = Column(Integer, ForeignKey('article.article_id', ondelete='CASCADE'), primary_key=True, autoincrement=False)
    name = Column(String(20), primary_key=True, index=True)
    create_dt = Column(Integer, nullable=False)
    update_dt = Column(Integer, nullable=False)

    def __init__(self):
        self.create_dt = int(time.mktime(datetime.now().timetuple()))
        self.update_dt = int(time.mktime(datetime.now().timetuple()))

    def __repr__(self):
        return "article_id: %s, name: %s, create_dt: %s, update_dt: %s" % (self.article_id, self.name, self.create_dt, self.update_dt)

    def list(self):
        return DBSession.query(ArticleTag).all()
