from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import *

engine = create_engine("postgresql://postgres:WRMNSXGol1@a8f213870167411ea9df302af6eaa18b-1639397014.eu-west-1.elb.amazonaws.com/wo-database")



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

result = set_bddClient("Test", "WO", "olv", "azerty", "old-ns")
print("creation de la base test :" + str(result))


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
#print("suppression de la ligne " + str(id))
#del_bddClient(4)

# _______________  ROUTES _______________

@app.route('/helloworld')
def helloworld():
    return 'Hello World!'


@app.route('/testdata', methods=['GET'])
def parse_request_get():
    data = get_listbddClient()
    return data


# @app.route('/testdata', methods=['POST'])
# def parse_request_post():
#     data = request.data  # Le payload de votre requete
#     print(str(data))
#     result = putData(data)
#     return result


if __name__ == '__main__':
    app.run("0.0.0.0")