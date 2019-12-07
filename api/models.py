from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Database(Base):
    __tablename__ = 'database'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Owner = Column(String)
    User = Column(String)
    Password = Column(String)
    Namespace = Column(String)

    def __repr__(self):
        return "<Database(Name='{}', Owner='{}', User='{}', Password='{}', Namespace='{}')>" \
            .format(self.Name, self.Owner, self.User, self.Password, self.Namespace)
