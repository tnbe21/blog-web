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
    admin_user_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(30), nullable=False)
    password = Column(Text, nullable=False)
    create_dt = Column(Integer, nullable=False, default=int(time.mktime(datetime.now().timetuple())))
    update_dt = Column(Integer, nullable=False, default=int(time.mktime(datetime.now().timetuple())))

    def __init__(self, admin_user_id, name, password):
        self.admin_user_id = admin_user_id
        self.name = name
        self.password = password
