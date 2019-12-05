from flask import *
from flask_cors import CORS
import json, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base, Database

app = Flask(__name__)
CORS(app)

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# _______________  CREATE DATABASE _______________
def create_db(session, Name, Owner, Namespace, User, Password):
	session.add(Database(Name, Owner, Namespace, User, Password))


# _______________  READ DATABASE _______________
def read_db(session):
    result = session.query(Database).all()
    data = []
    for i in result:
        read_json = {}
        read_json["Name"] = i.Name
        read_json["Owner"] = i.Owner
        read_json["Namespace"] = i.Namespace
        read_json["User"] = i.User
        read_json["Password"] = i.Password

        data.append(read_json)
    return data

# _______________  ROUTES _______________

#TEST CONNECTION
@app.route('/helloworld')
def hello_world():
    return 'Hello World!'

#READ
@app.route('/data', methods=['GET'])
def parse_request_get():
    session = Session()
    data = read_db(session)
    return json.dumps(data)

#CREATE
@app.route('/data', methods=['POST'])
def parse_request2():
    session = Session()
    param = request.data.decode('utf-8')
    result = create_db(session, param["Name"], param["Owner"], param["Namespace"], param["User"], param["Password"])
    return str(result)


if __name__ == '__main__':
    app.run("0.0.0.0")
