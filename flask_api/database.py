# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine('mysql+mysqldb://root:123456@127.0.0.1/weixin?charset=utf8')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Account(Base):
    __tablename__ = 'Account'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    createdtime = Column(DateTime)


class Relations(Base):
    __tablename__ = 'Relations'
    id = Column(Integer, primary_key=True)
    laccountid = Column(Integer)
    raccountid = Column(Integer)
    createdtime = Column(DateTime)

class Groups(Base):
    __tablename__ = 'Groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    createdtime = Column(DateTime)
