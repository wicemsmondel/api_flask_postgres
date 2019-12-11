import base64, os

USER = 'cG9zdGdyZXMK'
PASSWORD = 'TXlWOWV2VnlnZA=='
URI = 'bG9pY2stcG9zdGdyZXMtcG9zdGdyZXNxbC5wb3N0Z3Jlcy5zdmMuY2x1c3Rlci5sb2NhbAo='
PORT = 'NTQzMgo='
DATABASE = 'd28tZGF0YWJhc2UK'


user = base64.b64decode(USER).decode('ascii').rstrip()
password = base64.b64decode(PASSWORD).decode('ascii').rstrip()
uri = base64.b64decode(URI).decode('ascii').rstrip()
port = base64.b64decode(PORT).decode('ascii').rstrip()
database = base64.b64decode(DATABASE).decode('ascii').rstrip()

DATABASE_URI = 'postgres+psycopg2://{}:{}@{}:{}/{}'.format(user, password, uri, port, database)
print(DATABASE_URI)



