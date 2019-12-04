from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database(Base):
    __tablename__ = 'database'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Owner = Column(String)
    User = Column(String)
    Password = Column(String)
    Namespace = Column(String)
