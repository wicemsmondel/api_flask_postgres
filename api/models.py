from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Database(Base):
    __tablename__ = 'database'
    id = Column(Integer, primary_key=True)
    Nom = Column(String)
    owner = Column(String)
    user = Column(String)
    password = Column(String)
    namespace = Column(String)

    def __repr__(self):
        return "<Database(Nom='{}', owner='{}', user='{}', password='{}', namespace='{}')>" \
            .format(self.Nom, self.owner, self.user, self.password, self.namespace)
