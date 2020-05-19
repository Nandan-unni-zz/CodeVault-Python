import time
import imp

screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')

key = imp.load_source('key', './Settings/keys.py')

from pymongo import MongoClient
route = MongoClient("mongodb://localhost:27017") # Client : route
proton = route.proton # Database : proton
contacts = proton.contacts # Collection : contacts
notes = proton.notes # Collection : notes

def factory_reset():
    screen.clear()
    print("\n\n")
    print("Deleting Data...", end="")
    time.sleep(0.5)
    contacts.delete_many({})
    notes.delete_many({})
    key.default = {
        'time' : 24,
        'date' : 'number',
        'storage' : 'mongodb'
    }
    return None

def time_format():
    design.create_band('Select Time Format')
    opt = menu.create_3('24 hour', '12 hour', 'Cancel')
    if opt == '12 hour':
        key.mod_def('time', '12')
        return None
    elif opt == '24 hour':
        key.mod_def('time', '24')
        return None
    else:
        return None

def date_format():
    design.create_band('Select Month Display Method')
    opt = menu.create_3('Text', 'Number', 'Cancel')
    if opt == 'Text':
        key.mod_def('date', 'text')
    elif opt == 'Number':
        key.mod_def('date', 'number')