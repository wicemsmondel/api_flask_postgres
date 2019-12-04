from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    engine = create_engine("postgresql://postgres:WRMNSXGol1@a8f213870167411ea9df302af6eaa18b-1639397014.eu-west-1.elb.amazonaws.com:5432/wo-database")
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

#result = set_bddClient("newTest", "WO", "olv", "azerty", "test-ns")
#print("creation de la base test :" + str(result))


def get_listbddClient():
    allBdd = session.query(Database)
    bddClt=[]
    allbddClt=[]
    for bdd in allBdd:
        bddClt.append(bdd.Id)
        bddClt.append(bdd.Name)
        bddClt.append(bdd.Owner)
        bddClt.append(bdd.User)
        bddClt.append(bdd.Namespace)

        allbddClt.append(bddClt)    
    return allbddClt

testListBddClt=get_listbddClient()
print(testListBddClt)

def del_bddClient(id):
    session.query(Database).filter(Database.Id==id).delete()
    session.commit()
print("suppression de la ligne " + str(id))
del_bddClient(4)