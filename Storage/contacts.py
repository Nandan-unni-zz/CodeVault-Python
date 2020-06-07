from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

from colorama import Fore, Back, Style

from pymongo import MongoClient
route = MongoClient("mongodb://localhost:27017") # Client : route
proton = route.proton # Database : proton
contacts = proton.contacts # Collection : contacts

def add():
    design.create_band('ADD CONTACTS')
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
    design.create_band('CONTACTS')
    for contact in contacts.find().sort('name', 1):
        print(Fore.BLUE, Style.BRIGHT, contact['name'], Style.RESET_ALL, '    :  ', contact['phno'])
    print(Fore.MAGENTA)
    input("\n\t    Continue >> ")

def edit():
    view()
    design.create_head('EDIT CONTACT')
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
    design.create_head('DELETE CONTACT')
    remove = input("\n\n\tName : ")
    contacts.delete_one({'name' : remove})
    screen.clear()
    return None


if __name__ == '__main__':
    pass