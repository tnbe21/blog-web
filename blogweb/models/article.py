import time
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Column,
    Integer,
    SmallInteger,
    String,
    Text
)
from sqlalchemy.orm import relationship

from . import Base, DBSession
from articletag import ArticleTag

article_tag = ArticleTag.__table__


class Article(Base):
    __tablename__ = 'article'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    article_id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String(50), nullable=False)
    body = Column(Text, nullable=False)
    # 0: DRAFT, 1: PUBLIC, 10: DELETED
    status = Column(SmallInteger, nullable=False)
    create_dt = Column(BigInteger, nullable=False)
    update_dt = Column(BigInteger, nullable=False)

    tags = relationship('ArticleTag')

    def __init__(self):
        self.create_dt = int(time.mktime(datetime.now().timetuple()))
        self.update_dt = int(time.mktime(datetime.now().timetuple()))

    def __repr__(self):
        return '{article_id: %s, title: %s, create_dt: %s, update_dt: %s}'\
            % (self.article_id, self.title, self.create_dt, self.update_dt)

    def get(self, id):
        return DBSession.query(Article).filter(Article.article_id == id).first()

    def list(self, from_dt, to_dt, tag, from_idx, to_idx):
        query = DBSession.query(Article)

        if tag is not None:
            article_ids = [article_tag.article_id for article_tag in ArticleTag().findByName(tag)]
            query = query.filter(Article.article_id.in_(article_ids))

        query = query.filter(Article.status == 1)

        if from_dt > 0 and to_dt > 0:
            query = query.filter(Article.create_dt >= from_dt).filter(Article.create_dt <= to_dt)

        return query.order_by(Article.article_id.desc())[from_idx:to_idx]

    def current_title_list(self):
        return DBSession.query(Article.article_id, Article.title)\
            .filter(Article.status == 1).order_by(Article.article_id.desc()).limit(5)
