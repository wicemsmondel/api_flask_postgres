from flask import *
from flask import request
from flask_cors import CORS
import json
import jsonify
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base, Database

app = Flask(__name__)
CORS(app)

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# _______________  CREATE DATABASE _______________
def create_db(name, owner, user, password, namespace):
    db = Database(
        Name=name,
        Owner=owner,
        User=user,
        Password=password,
        Namespace=namespace
    )
    session.add(db)
    session.commit()
    # return 0

# result = create_db("fridayTest3", "WO", "Wicem", "psw", "wo-ns")


# _______________  GET DATABASE _______________
def get_data(session):
    result = session.query(Database).all()
    data = []
    for i in result:
        get_json = {
            "Id": i.Id,
            "Name": i.Name,
            "Owner": i.Owner,
            "Namespace": i.Namespace,
            "User": i.User,
            "Password": i.Password
        }
        data.append(get_json)
    return (data)

# _______________  POST DATABASE _______________


def post_data(data):
    sqldata = json.loads(data)
    print(data)
    print(sqldata)
    tableEntry = Database(
        Id=int(sqldata["Id"]),
        Name=sqldata["Name"],
        Owner=sqldata["Owner"],
        User=sqldata["User"],
        Password=sqldata["Password"],
        Namespace=sqldata["Namespace"],
    )
    session.add(tableEntry)
    session.commit()


# _______________  DELETE DATABASE _______________

def delData(numb):
    query = session.query(Database).filter_by(Id=numb)
    session.delete(query.one())
    session.commit()
    return "TRUE"

# _______________  ROUTES _______________

# TEST CONNECTION
@app.route('/')
def hello_world():
    return 'Hello World!'

# READ
@app.route('/data', methods=['GET'])
def parse_request_get():
    session = Session()
    data = get_data(session)
    return json.dumps(data)

# CREATE
@app.route('/data', methods=['POST'])
def parse_request_post():
    data = request.data
    print(request.data)
    try:
        post_data(data)
        success = 'True'
    except:
        print('failed')
        sys.exit(1)
    return success

# DELETE
@app.route('/data/<numb>', methods=['DELETE'])
def api_article(numb):
    delData(numb)
    return 'Vous avez supprimer ' + numb


if __name__ == '__main__':
    app.run('0.0.0.0')
