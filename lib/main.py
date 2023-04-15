from peewee import *

db = PostgresqlDatabase(
  'Contacts', 
  user='',
  password='',
  host='localhost', 
  port=5432 
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()
    address = CharField(max_length=350)
    city = CharField()
    zipcode = IntegerField()
    # contact_added = DateTimeField()
    # favorite = True

db.drop_tables([Person])
db.create_tables([Person])


