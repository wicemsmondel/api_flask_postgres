from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base

engine = create_engine(DATABASE_URI)


Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

app = Flask(__name__)
CORS(app)

def fermeture(session):
    session.flush()
    session.commit()
    session.close()

#_______________  ROUTES _______________

@app.route('/v1/hello-world')
def hello_world():
    return 'Hello World!'

#READ
@app.route('/database', methods=['GET'])
def parse_request():
    # Votre fonction pour lire
    session = Session()
    data =readDatabase(session)
    fermeture(session)
    return json.dumps(data)

#CREATE
@app.route('/database', methods=['POST'])
def parse_request2():
    session = Session()
    param = request.data.decode('utf-8')
    result = createDatabase(session, param["Name"], param["Owner"], param["Namespace"], param["User"], param["Password"])
    fermeture(session)
    return str(result)

@app.route('/database/update', methods=['POST'])
def update_request():
    session = Session()
    param = request.data.decode('utf-8')
    result = updateDatabase(session, param["Id"], param["Name"], param["Owner"], param["Namespace"], param["User"], param["Password"])
    fermeture(session)
    return str(result)

#DELETE
@app.route('/database/<numb>', methods=['DELETE'])
def delete_request(numb):
    # Votre fonction pour supprimer les data d'un fichier
    session = Session()
    result = deleteDatabase(session, numb)
    fermeture(session)
    return str(result)

if __name__ == '__main__':
    app.run("0.0.0.0")