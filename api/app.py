from flask import *
from flask import request
from flask_cors import CORS
import sys, json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base, Database

app = Flask(__name__)
CORS(app)

engine = create_engine(DATABASE_URI, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = Session()


def hibernate(session):
    session.commit()
    session.flush()
    session.close()


# _______________  FUNCTIONS _______________

##GET
def get_data(session):
    result = session.query(Database).all()
    data = []
    for i in result:
        get_json = {
            "Id": i.Id, 
            "Name": i.Name, 
            "Owner": i.Owner, 
            "User": i.User, 
            "Password": i.Password, 
            "Namespace": i.Namespace
            }
        data.append(get_json)
    return (data)


##POST
def post_data(data):
    sqldata = json.loads(data)
    print(sqldata)
    tableEntry = Database(
                Name=sqldata["Name"],
                Owner=sqldata["Owner"],
                User=sqldata["User"],
                Password=sqldata["Password"],
                Namespace=sqldata["Namespace"],
            )
    session.add(tableEntry)
    # hibernate(session)


##DELETE
def delete_data(numb):
    query = session.query(Database).filter_by(Id=numb)
    session.delete(query.one())
    hibernate(session)
    return ("Done")



# _______________  ROUTES _______________

##HOME
@app.route('/')
def hello_world():
    return 'Hello World!'


##GET
@app.route('/data', methods=['GET'])
def parse_request_get():
        try:
            data = get_data(session)
            hibernate(session)
        except:
            session.rollback()
        return str(json.dumps(data))


##POST
@app.route('/data', methods=['POST'])
def parse_request_post():
    data = request.data 
    print(request.data)
    try:
        post_data(data)
        session.commit()
    except:
        session.rollback()
        raise
    return data
    


##DELETE
@app.route('/data/<numb>', methods=['DELETE'])
def parse_request_delete(numb):
    try:
        erased = delete_data(numb)
        session.delete()
    except:
        session.flush
    return json.dumps(erased)


##RUN API
if __name__ == '__main__':
    app.run('0.0.0.0')

