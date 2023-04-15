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


db.create_tables([Contacts])


def Create():
    create_running = True
    while create_running:
        
        print('<------/------>')
        print("Add new contact:")

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
        
        print('<------/------>')
        print('Would you like to add another contact?: Yes(y) No(n)')
        input_next = input('-> ')
        next_res = str(input_next)

        if next_res.lower() == 'y':
            create_running = True
        else:
            create_running = False
            break


def Help():
    print('<------/------>')
    print('HELP SCREEN')
    print('Add -> Create a new contact, First Name, Last Name & Phone Number are REQUIRED.')
    print('Find -> Find a contact by Last Name or ID.')
    print('Help -> Opens HELP SCREEN')
    print('End -> Exit Contacts')

def Find():
    
    find_running = True
    while find_running:
        
        print('<------/------>')
        print('Find contact by Last Name or ID.')

        input_find = input('-> ')
        find_res = str(input_find)

        contact = Contacts.select().where((Contacts.last_name == find_res) | (Contacts.id == find_res))
        
        for person in contact:
            print('<------/------>')
            print('    First Name: {} \n     Last Name: {} \n  Phone Number: {} \n         Email: {} \nAddress line 1: {} \nAddress line 2: {} \n          City: {} \n       Zipcode: {} \n         Notes: {}'
                  .format(person.first_name, 
                          person.last_name, 
                          person.phone_number, 
                          person.email, 
                          person.address1, 
                          person.address2, 
                          person.city, 
                          person.zipcode, 
                          person.note
                          ))
            
        print('<------/------>')
        print('Would you like to Find another contact?: Yes(y) No(n)')
        input_next = input('-> ')
        next_res = str(input_next)

        if next_res.lower() == 'y':
            find_running = True
        else:
            find_running = False
            break


def Start():
    
    start_running = True
    while start_running:

        print('<------/------>')
        print('Welcome to Contacts')
        print('To get started type: Find, Add, Help, End')

        input_start = input('-> ')
        start_res = str(input_start)

        if start_res.lower() == 'add':
            Create()
        elif start_res.lower()== 'help':
            Help()
        elif start_res.lower()== 'find':
            Find()
        else:
            print('<------/------>')
            print('Thank You for using Contacts!')
            print('<------/------>')
            start_running = False
            break

             
Start()