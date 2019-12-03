from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Compte, Bucket
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

#Create Compte
compte = Compte(
    Nom="Super Client",
    Description="Trop bien ce client"
)
session.add(compte)
session.commit()

def set_bddClient (nameBddClt, ownerBddClt, userBddClt, passwdBddClt, nsBddClt):
    BddClt = wo-table(
    Name= nameBddClt,
    Owner= ownerBddClt,
    User= userBddClt,
    Password= passwdBddClt,
    Namespace= nsBddClt
    )
    session.add(BddClt)
    session.commit()

set_bddClient("nomTest", "WO", "user", "azerty", "test-ns")


# Delete bdd
#def delete_bddClient(idbddClient):
#   session.delete(idbddClient)
#   session.commit()
