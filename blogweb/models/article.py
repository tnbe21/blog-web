import time
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    SmallInteger,
    String,
    Text
)
from sqlalchemy.orm import relation

from . import Base, DBSession
from articletag import ArticleTag

article_tag = ArticleTag.__table__


class Article(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String(50), nullable=False)
    body = Column(Text, nullable=False)
    # 0: DRAFT, 1: PUBLIC, 10: PRIVATE
    status = Column(SmallInteger, nullable=False)
    create_dt = Column(Integer, nullable=False)
    update_dt = Column(Integer, nullable=False)

    tags = relation('Tag', secondary=article_tag, backref='article')

    def __init__(self):
        self.create_dt = int(time.mktime(datetime.now().timetuple()))
        self.update_dt = int(time.mktime(datetime.now().timetuple()))

    def get(self, id):
        return DBSession.query(Article).filter_by(article_id=id).first()

    def list(self, from_dt, to_dt, tag, page):
        LIMIT_PER_PAGE = 3
        if from_dt > 0 and to_dt > 0:
            create_dt_filter_query = "create_dt >= %d and create_dt <= %d" % (from_dt, to_dt)
            return DBSession.query(Article).filter(create_dt_filter_query).order_by(Article.article_id.desc())[page:(page + LIMIT_PER_PAGE - 1)]
        else:
            return DBSession.query(Article).order_by(Article.article_id.desc())[page:(page + LIMIT_PER_PAGE - 1)]
