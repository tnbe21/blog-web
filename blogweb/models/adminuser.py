import time
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
    )

from . import Base


class AdminUser(Base):
    __tablename__ = 'admin_user'
    name = Column(String(30), primary_key=True, nullable=False)
    password = Column(Text, nullable=False)
    create_dt = Column(Integer, nullable=False)
    update_dt = Column(Integer, nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.create_dt = int(time.mktime(datetime.now().timetuple()))
        self.update_dt = int(time.mktime(datetime.now().timetuple()))
