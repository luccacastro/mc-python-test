import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    status = Column(Boolean, default=True)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    stopped_at = Column(DateTime, default=None)
    def __init__(self, message):
        self.message = message


engine = create_engine('sqlite:///sqlalchemy.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
