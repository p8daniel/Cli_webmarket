from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'webmarket',
    user='webmarket',
    password='webmarket',
    host='localhost', port=5000,
    autorollback=True
)
