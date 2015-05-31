from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    DateTime
    )

from . import Base


class AdminUser(Base):
    __tablename__ = 'admin_users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)


Index('admin_user_index', AdminUser.id, unique=True, mysql_length=255)
