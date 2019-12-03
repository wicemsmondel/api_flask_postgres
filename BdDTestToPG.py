from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    engine = create_engine("postgresql://postgres:WRMNSXGol1@a3c7d191f15bb11ea9df302af6eaa18b-1278716746.eu-west-1.elb.amazonaws.com:5432/wo-database")
except:
    print("ERROR IN CONNECTION")

print("END TEST CONNECTION")

Base = declarative_base()

class Database(Base):
    __tablename__ = 'database'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Owner = Column(String)
    User = Column(String)
    Password = Column(String)
    Namespace = Column(String)  

    def create(self, myId, myName, myOwner, myUser, myPwd, myNs):
        self.id=myId
        self.Name=myName
        self.Owner=myOwner
        self.User=myUser
        self.Password=myPwd
        self.Namespace=myNs

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def set_bddClient (nameBddClt, ownerBddClt, userBddClt, passwdBddClt, nsBddClt):
    BddClt = Database(
    Name= nameBddClt,
    Owner= ownerBddClt,
    User= userBddClt,
    Password= passwdBddClt,
    Namespace= nsBddClt
    )
    session.add(BddClt)
    session.commit()
    return 0

result = set_bddClient("nomTest", "WO", "user", "azerty", "test-ns")
print("creation de la base test :" + str(result))
