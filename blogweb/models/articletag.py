import time
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String
)

from . import Base


class ArticleTag(Base):
    __tablename__ = 'article_tag'
    article_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(20), primary_key=True, autoincrement=False)
    create_dt = Column(Integer, nullable=False)
    update_dt = Column(Integer, nullable=False)

    def __init__(self):
        self.create_dt = int(time.mktime(datetime.now().timetuple()))
        self.update_dt = int(time.mktime(datetime.now().timetuple()))
