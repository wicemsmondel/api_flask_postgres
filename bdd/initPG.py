import sqlalchemy
from sqlalchemy import create_engine
print(sqlalchemy.__version__)
engine = create_engine('postgresql://postgres:toor@localhost:5432/crudDB')


print("debut du TP ORM")