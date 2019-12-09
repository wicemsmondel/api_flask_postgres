# import os


# postgres_user = os.environ['POST_USER'].rstrip()
# postgres_pass = os.environ['POST_PASSWORD'].rstrip()
# uri = os.environ['URI_POSTGRES'].rstrip()
# port = os.environ['POST_PORT'].rstrip()
# dbase = os.environ['DBASE'].rstrip()

# DATABASE_URI = 'postgres+psycopg2://{}:{}@{}:{}/{}'.format(postgres_user, postgres_pass, uri, port, dbase)

DATABASE_URI = 'postgres+psycopg2://postgres:MyV9evVygd@a96461127173f11ea9df302af6eaa18b-663817862.eu-west-1.elb.amazonaws.com:5432/wo-database'
# DATABASE_URI = 'postgres+psycopg2://postgres:admin@localhost:5432/wo-database'