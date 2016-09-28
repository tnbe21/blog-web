import time
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String
)

from . import Base, DBSession


class Tag(Base):
    __tablename__ = 'tag'
    tag_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(20))
    create_dt = Column(Integer, nullable=False)
    update_dt = Column(Integer, nullable=False)

    def __json__(self, request):
        return {
            'tag_id': self.tag_id,
            'name': self.name
        }

    def __init__(self):
        self.create_dt = int(time.mktime(datetime.now().timetuple()))
        self.update_dt = int(time.mktime(datetime.now().timetuple()))

    def list(self):
        return DBSession.query(Tag).all()
