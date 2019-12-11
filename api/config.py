# import os, base64


# user = os.environ['USER'].rstrip()
# password = os.environ['PASSWORD'].rstrip()
# uri = os.environ['URI'].rstrip()
# port = os.environ['PORT'].rstrip()
# database = os.environ['DATABASE'].rstrip()

# DATABASE_URI = 'postgres+psycopg2://{}:{}@{}:{}/{}'.format(user, password, uri, port, database)

DATABASE_URI = 'postgres+psycopg2://postgres:MyV9evVygd@a96461127173f11ea9df302af6eaa18b-663817862.eu-west-1.elb.amazonaws.com:5432/wo-database'
# DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/wo-database'