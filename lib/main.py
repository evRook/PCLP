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
    # note = TextField()
    # contact_updated = DateTimeField()
    # favorite = True

db.drop_tables([Contacts])
db.create_tables([Contacts])

running = True
while running:
    
    input_first = input('First name of contact: ')
    first_res = str(input_first)

    input_last = input('Last name of contat: ')
    last_res = str(input_last) 

    new_contact = Contacts(
      first_name = first_res, 
      last_name = last_res 
      # phone_number = '123-456-7890',
      # email = 'Eric@email.com',
      # address= '42 walaby way',
      # city = 'Sydney',
      # zipcode = 90192,
      
      )

    new_contact.save()

    input_next = input('Would you like to add another contact?: Yes(y) No(n) ')
    next_res = str(input_next)

    if next_res == 'y':
        print('Add another contact:')
        running = True
    else:
        running = False
        break
    