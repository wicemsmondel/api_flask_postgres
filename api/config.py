import os, base64


user_encoded = os.environ['USER']
password_encoded = os.environ['PASSWORD']
uri_encoded = os.environ['URI']
port_encoded = os.environ['PORT']
database_encoded = os.environ['DATABASE']

user_decoded = base64.b64decode(user_encoded).decode('ascii').rstrip()
password_decoded = base64.b64decode(password_encoded).decode('ascii').rstrip()
uri_decoded = base64.b64decode(uri_encoded).decode('ascii').rstrip()
port_decoded = base64.b64decode(port_encoded).decode('ascii').rstrip()
database_decoded = base64.b64decode(database_encoded).decode('ascii').rstrip()

DATABASE_URI = 'postgres+psycopg2://{}:{}@{}:{}/{}'.format(user_decoded, password_decoded, uri_decoded, port_decoded, database_decoded)

# print(DATABASE_URI)
# DATABASE_URI = 'postgres+psycopg2://postgres:MyV9evVygd@a96461127173f11ea9df302af6eaa18b-663817862.eu-west-1.elb.amazonaws.com:5432/wo-database'
# DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/wo-database'