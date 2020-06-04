from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

from pymongo import MongoClient
route = MongoClient("mongodb://localhost:27017") # Client : route
proton = route.proton # Database : proton
contacts = proton.contacts # Collection : contacts

def add():
    screen.clear()
    print("\n\n\tA D D   C O N T A C T S")
    cname=input("\n\tName : ")
    cphno=input("\tPhone Number : ")
    screen.clear()
    person = {
        'name' : cname,
        'phno' : cphno
    }
    contacts.insert_one(person)
    opt = menu.create_2('Add Contact', 'Back')
    if opt == 'Add Contact':
        add()
    else:
        return None

def view():
    screen.clear()
    print("\n\n\t\tC O N T A C T S\n")
    for contact in contacts.find().sort('name', 1):
        print(contact['name'], '\t :  ', contact['phno'])
    input("\n\t    Continue >> ")

def edit():
    view()
    print("\n\n\tE D I T   C O N T A C T")
    old = input("\n\n\tSearch by Name : ")
    opt = menu.create_2('Edit Name', 'Edit Phone Number')
    if opt == 'Edit Name':
        new = input("\n\tNew Name : ")
        contacts.update_one({'name' : old}, {'$set': {'name' : new}})
    else:
        new = input("\n\tNew Phone Number : ")
        contacts.update_one({'name' : old}, {'$set': {'phno' : new}})
    screen.clear()
    return None

def delete():
    view()
    print("\n\n\t D E L E T E   C O N T A C T")
    remove = input("\n\n\tName : ")
    contacts.delete_one({'name' : remove})
    screen.clear()
    return None


if __name__ == '__main__':
    pass