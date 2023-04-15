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
    phone_number = CharField()
    email = CharField(null = True)
    address1 = CharField(null = True, max_length=350)
    address2 = CharField(null = True)
    city = CharField(null = True)
    zipcode = CharField(null = True)
    note = TextField(null = True)
    # contact_updated = DateTimeField()
    # favorite = True

db.drop_tables([Contacts])
db.create_tables([Contacts])

# def Start():
    
#     start_running = True
#     while start_running:
      
#         print('Welcome to Contacts')
#         print('To get started type: Add, Delete, Update, Find, Help')

#         input_start = input('-> ')
#         start_res = str(input_start)

#         if start_res.lower == 'add':
#             Create()
          
# Start()


def Create():
    running = True
    while running:
        
        input_first = input('First Name: ')
        first_res = str(input_first)

        input_last = input('Last Name: ')
        last_res = str(input_last) 

        input_phone = input('Phone Number: ')
        phone_res = str(input_phone) 

        input_email = input('Email address: ')
        email_res = str(input_email) 

        input_add1 = input('Address line 1: ')
        add1_res = str(input_add1) 

        input_add2 = input('Address line 2: ')
        add2_res = str(input_add2) 

        input_city = input('City: ')
        city_res = str(input_city) 

        input_zip = input('Zipcode: ')
        zip_res = str(input_zip)

        input_note = input('Notes: ')
        note_res = str(input_note)

        new_contact = Contacts(
          first_name = first_res, 
          last_name = last_res, 
          phone_number = phone_res,
          email = email_res,
          address1 = add1_res,
          address2 = add2_res,
          city = city_res,
          zipcode = zip_res,
          note = note_res
        )

        new_contact.save()

        input_next = input('Would you like to add another contact?: Yes(y) No(n) ')
        next_res = str(input_next)

        if next_res.lower() == 'y':
            print('Add another contact:')
            running = True
        else:
            running = False
            break


