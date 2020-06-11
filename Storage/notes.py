from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

from colorama import Fore, Back, Style

from pymongo import MongoClient
route = MongoClient("mongodb://localhost:27017") # Client : route
proton = route.proton # Database : proton
notes = proton.notes # Collection : notes

def add():
    design.create_band('ADD NOTES ➕')
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
    design.create_band('NOTES')
    for note in notes.find().sort('title', 1):
        print(Fore.BLUE, Style.BRIGHT, note['title'], Style.RESET_ALL)
        print("\n", note['text'], "\n\n")
    print(Fore.MAGENTA)
    input("\n\t    Continue >> ")

def delete():
    design.create_band('DELETE NOTE ⛔️')
    remove  = input("\n\n\tTitle : ")
    notes.delete_one({'title' : remove})
    screen.clear()
    return None


if __name__ == '__main__':
    pass