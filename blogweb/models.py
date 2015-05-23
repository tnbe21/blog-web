from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Text,
    DateTime
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    author = Column(String)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)

Index('article_index', Article.id, unique=True, mysql_length=255)

class AdminUser(Base):
    __tablename__ = 'admin_users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)

Index('admin_user_index', AdminUser.id, unique=True, mysql_length=255)
