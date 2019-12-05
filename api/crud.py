from flask import *
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base, Database

app = Flask(__name__)

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def set_bddClient(nameBddClt, ownerBddClt, userBddClt, passwdBddClt, nsBddClt):
    BddClt = Database(
        Name=nameBddClt,
        Owner=ownerBddClt,
        User=userBddClt,
        Password=passwdBddClt,
        Namespace=nsBddClt
    )
    session.add(BddClt)
    session.commit()
    return 0


result = set_bddClient("newTest", "WO", "wicem", "azerty", "wicem-ns")
print("creation de la base test :" + str(result))


def get_listbddClient():
    allBdd = session.query(Database)
    bddClt = []
    allbddClt = []
    for bdd in allBdd:
        bddClt.append(bdd.Id)
        bddClt.append(bdd.Name)
        bddClt.append(bdd.Owner)
        bddClt.append(bdd.User)
        bddClt.append(bdd.Namespace)
        allbddClt.append(bddClt)
    return allbddClt


testListBddClt = get_listbddClient()
print(testListBddClt)


def del_bddClient(id):
    session.query(Database).filter(Database.Id == id).delete()
    session.commit()


print("suppression de la ligne" + str(id))
del_bddClient(5)


# _______________  ROUTES _______________

@app.route('/helloworld')
def hello_world():
    return 'Hello World!'


@app.route('/data', methods=['GET'])
def parse_request_get():
    data = get_listbddClient()
    return data


@app.route('/data', methods=['POST'])
def parse_request_post():
    data = request.data  
    print(str(data))
    result = set_bddClient(data)
    return result


if __name__ == '__main__':
    app.run("0.0.0.0")
