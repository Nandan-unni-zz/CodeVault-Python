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