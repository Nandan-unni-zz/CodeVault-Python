from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

from pymongo import MongoClient
route = MongoClient("mongodb://localhost:27017") # Client : route
proton = route.proton # Database : proton
notes = proton.notes # Collection : notes

def add():
    screen.clear()
    print("\n\n\tA D D   N O T E S")
    ntitle=input("\n\tTitle : ")
    ntext=input("\n Type notes and press enter to save : \n\n    ")
    screen.clear()
    note = {
        'title' : ntitle,
        'text' : ntext
    }
    notes.insert_one(note)
    opt = menu.create_2('Add Notes', 'Back')
    if opt == 'Add Notes':
        add()
    else:
        return None

def view():
    screen.clear()
    print("\n\n\t\tC O N T A C T S\n")
    for note in notes.find().sort('title', 1):
        print(note['title'])
        print("\n", note['text'], "\n\n")
    return None

def delete():
    screen.clear()
    print("\n\n\tD E L E T E   N O T E S")
    a=input("\n\n\tTitle : ")
    notes.delete_one({'title' : a})
    return None


if __name__ == '__main__':
    pass