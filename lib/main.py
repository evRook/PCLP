from peewee import *

db = PostgresqlDatabase(
  'contacts', 
  user='',
  password='',
  host='localhost', 
  port=5432
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contacts(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    # phone_number = CharField(default = '')
    # email = CharField(default = '')
    # address = CharField(default = '', max_length=350)
    # city = CharField(default = '')
    # zipcode = IntegerField(default = None)
    # contact_updated = DateTimeField()
    # favorite = True

# db.drop_tables([Contacts])
db.create_tables([Contacts])

# eric = Contacts(
#   first_name = 'Eric', 
#   last_name = 'Spychalski', 
#   phone_number = '123-456-7890',
#   email = 'Eric@email.com',
#   address= '42 walaby way',
#   city = 'Sydney',
#   zipcode = 90192
#   )

# eric.save()
# running = True
# while running:

def new_contact():
    
    input_first = input('First name of contact: ')
    first_res = str(input_first)

    input_last = input('Last name of contat: ')
    last_res = str(input_last) 

    

    eric = Contacts(
      first_name = first_res, 
      last_name = last_res 
      # phone_number = '123-456-7890',
      # email = 'Eric@email.com',
      # address= '42 walaby way',
      # city = 'Sydney',
      # zipcode = 90192
      )

    eric.save()

new_contact()