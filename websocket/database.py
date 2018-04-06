# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME

engine = create_engine('mysql+mysqldb://root:123456@127.0.0.1/weixin?charset=utf8')
Base = declarative_base()


# 创建会话
def create_session():
    db_session = sessionmaker(bind=engine)
    return db_session()


class Chats(Base):
    __tablename__ = 'Chats'
    id = Column(Integer, primary_key=True)
    sendid = Column(Integer)
    recid = Column(Integer)
    msg = Column(String)
    createdtime = Column(DATETIME)
