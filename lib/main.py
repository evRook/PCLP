from peewee import *
import datetime

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
    address1 = CharField(null = True, max_length = 350)
    address2 = CharField(null = True)
    city = CharField(null = True)
    state = CharField(null = True)
    country = CharField(null = True)
    zipcode = CharField(null = True)
    note = TextField(null = True)
    created = DateTimeField(default = datetime.datetime.now())

# db.drop_tables([Contacts])
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

        input_state = input('State: ')
        state_res = str(input_state) 

        input_country = input('Country: ')
        country_res = str(input_country)

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
          state = state_res,
          country = country_res,
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
    print('Find -> Find a contact by Last Name.')
    print('Add -> Create a new contact, First Name, Last Name & Phone Number are REQUIRED.')
    print('Update -> Update contact info by ID.')
    print('Delete -> Delete contact info by ID.')
    print('Help -> Opens HELP SCREEN.')
    print('End -> Exit Contacts.')


def Find():
    
    find_running = True
    while find_running:
        
        print('<------/------>')
        print('Find contact by Last Name.')

        input_find = input('-> ')
        find_res = str(input_find)
        contact = Contacts.select().where((Contacts.last_name == find_res))
        all_contacts = Contacts.select()

        if find_res.lower() == "all":
            for person in all_contacts:
                print('<------/------>')
                print('            ID: {} \n    First Name: {} \n     Last Name: {} \n  Phone Number: {} \n         Email: {} \nAddress line 1: {} \nAddress line 2: {} \n          City: {} \n         State: {} \n       Country: {} \n       Zipcode: {} \n         Notes: {} \n       Created: {}'
                      .format(person.id,
                              person.first_name, 
                              person.last_name, 
                              person.phone_number, 
                              person.email, 
                              person.address1, 
                              person.address2, 
                              person.city, 
                              person.state,
                              person.country,
                              person.zipcode, 
                              person.note,
                              person.created
                              ))
        else:
            for person in contact:
                print('<------/------>')
                print('            ID: {} \n    First Name: {} \n     Last Name: {} \n  Phone Number: {} \n         Email: {} \nAddress line 1: {} \nAddress line 2: {} \n          City: {} \n         State: {} \n       Country: {} \n       Zipcode: {} \n         Notes: {} \n       Created: {}'
                      .format(person.id,
                              person.first_name, 
                              person.last_name, 
                              person.phone_number, 
                              person.email, 
                              person.address1, 
                              person.address2, 
                              person.city, 
                              person.state,
                              person.country,
                              person.zipcode, 
                              person.note,
                              person.created
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

def Delete():
    
    delete_running = True
    while delete_running:
        
        print('<------/------>')
        print('Delete contact by ID.')

        input_delete = input('-> ')
        delete_res = str(input_delete)

        del_contact = Contacts.get(Contacts.id == delete_res)
        del_contact.delete_instance()

        print('<------/------>')
        print('Would you like to Delete another contact?: Yes(y) No(n)')
        input_next = input('-> ')
        next_res = str(input_next)

        if next_res.lower() == 'y':
            delete_running = True
        else:
            delete_running = False
            break
        
def Update():
    
    update_running = True
    while update_running:
        
        print('<------/------>')
        print('Update contact by ID.')

        input_id = input('-> ')
        id_res = str(input_id)

        id_select = Contacts.select().where(Contacts.id == id_res)

        for person in id_select:
                print('<------/------>')
                print('            ID: {} \n    First Name: {} \n     Last Name: {} \n  Phone Number: {} \n         Email: {} \nAddress line 1: {} \nAddress line 2: {} \n          City: {} \n         State: {} \n       Country: {} \n       Zipcode: {} \n         Notes: {} \n       Created: {}'
                      .format(person.id,
                              person.first_name, 
                              person.last_name, 
                              person.phone_number, 
                              person.email, 
                              person.address1, 
                              person.address2, 
                              person.city, 
                              person.state,
                              person.country,
                              person.zipcode, 
                              person.note,
                              person.created
                              ))

        print('<------/------>')
        print('What would you like to update?')
        print('First, Last, Phone, Email, Address1, Address2, City, State, Country, Zipcode, Note')

        input_spec = input('-> ')
        spec_res = str(input_spec) 

        print('<------/------>')
        print('Update too:')

        input_update = input('-> ')
        update_res = str(input_update)

        update_contact = Contacts.get(Contacts.id == id_res)
        
        if spec_res.lower() == 'first':
            update_contact.first_name = update_res
            update_contact.save()
        elif spec_res.lower() == 'last':
            update_contact.last_name = update_res
            update_contact.save()
        elif spec_res.lower() == 'phone':
            update_contact.phone_number = update_res
            update_contact.save()
        elif spec_res.lower() == 'email':
            update_contact.email = update_res
            update_contact.save()
        elif spec_res.lower() == 'address1':
            update_contact.address1 = update_res
            update_contact.save()
        elif spec_res.lower() == 'address2':
            update_contact.address2 = update_res
            update_contact.save()
        elif spec_res.lower() == 'city':
            update_contact.city = update_res
            update_contact.save()
        elif spec_res.lower() == 'state':
            update_contact.state = update_res
            update_contact.save()
        elif spec_res.lower() == 'country':
            update_contact.country = update_res
            update_contact.save()
        elif spec_res.lower() == 'zipcode':
            update_contact.zipcode = update_res
            update_contact.save()
        elif spec_res.lower() == 'note':
            update_contact.note = update_res
            update_contact.save()
        else:
            print('<------/------>')
            print(f'COMMAND {spec_res} NOT RECOGNIZED')
            print('Must input: \nFirst \nLast \nPhone \nEmail \nAddress1 \nAddress2 \nCity \nSate \nCountry \nZipcode \nNote')

        print('<------/------>')
        print('Would you like to Update another contact?: Yes(y) No(n)')
        input_next = input('-> ')
        next_res = str(input_next)

        if next_res.lower() == 'y':
            update_running = True
        else:
            update_running = False
            break

def Start():
    
    start_running = True
    while start_running:

        print('<------/------>')
        print('Welcome to Contacts')
        print('To get started type: Find, Add, Update, Delete, Help, End')

        input_start = input('-> ')
        start_res = str(input_start)

        if start_res.lower() == 'add':
            Create()
        elif start_res.lower()== 'help':
            Help()
        elif start_res.lower()== 'find':
            Find()
        elif start_res.lower()== 'delete':
            Delete()
        elif start_res.lower()== 'update':
            Update()
        elif start_res.lower() == 'end':
            print('<------/------>')
            print('Thank You for using Contacts!')
            print('<------/------>')
            start_running = False
            break
        else:
            print('<------/------>')
            print(f'COMMAND "{start_res}" NOT FOUND')
            Help()
          
Start()