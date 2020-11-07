from Settings import keys as key
from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

import time
from pymongo import MongoClient

route = MongoClient("mongodb://localhost:27017") # Client : route
proton = route.proton # Database : proton
contacts = proton.contacts # Collection : contacts
notes = proton.notes # Collection : notes

def factory_reset():
    screen.clear()
    print("\n\n")
    screen.clear()
    contacts.delete_many({})
    notes.delete_many({})
    key.mod_def('time', '12')
    key.mod_def('date', 'text')
    return None


if __name__ == '__main__':
    pass