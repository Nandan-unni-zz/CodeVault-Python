'''
DOCSTRING: A Sample OS of a feature phone made using Python just for learning purpose.
'''
##### A S NANDANUNNI #####
#### IG : u.n.n.i._ ######
#### GH : nandan-unni ####

import sys

from Apps import calculator
from Apps import hangman
from Apps import hand_cricket
from Apps import tic_tac_toe

from Settings import settings
from Settings import date_time

from Storage import contacts
from Storage import notes

from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen


def home():
    '''
    DOCSTRING: A function which controls the homescreen and connects to the inner elements.
    '''
    screen.clear()
    date_time.timer()
    opt = menu.create_7('CONTACTS 👤', 'NOTES 📚',
                        'CALCULATOR 📟', 'SETTINGS 🔧',
                        'GAMES ⚽️', 'REFRESH 🌀',
                        'POWER OFF 🛑')
    design.create_band(opt)
    if opt == 'CONTACTS 👤':
        subopt = menu.create_5('Add Contact', 'View Contacts',
                               'Edit Contacts', 'Delete Contacts', 'Back')
        if subopt == 'Add Contact':
            contacts.add()
            home()
        elif subopt == 'View Contacts':
            contacts.view()
            home()
        elif subopt == 'Edit Contacts':
            contacts.edit()
            home()
        elif subopt == 'Delete Contacts':
            contacts.delete()
            home()
        else:
            home()
    elif opt == 'NOTES 📚':
        subopt = menu.create_4('New Note', 'View Notes', 'Delete Notes', 'Back')
        if subopt == 'New Note':
            notes.add()
            home()
        elif subopt == 'View Notes':
            notes.view()
            home()
        elif subopt == 'Delete Notes':
            notes.delete()
            home()
        else:
            home()

    elif opt == 'CALCULATOR 📟':
        calculator.main()
        home()

    elif opt == 'SETTINGS 🔧':
        subopt = menu.create_4('Date', 'Time', 'Factory Reset', 'Back')
        if subopt == 'Time':
            date_time.time_format()
            home()
        elif subopt == 'Date':
            date_time.date_format()
            home()
        elif subopt == 'Factory Reset':
            settings.factory_reset()
            home()
        else:
            home()
    elif opt == 'GAMES ⚽️':
        subopt = menu.create_4('Hangman', 'Tic Tac Toe', 'Hand Cricket', 'Back')
        if subopt == 'Hangman':
            hangman.main()
            home()
        elif subopt == 'Tic Tac Toe':
            tic_tac_toe.main()
            home()
        elif subopt == 'Hand Cricket (dev)':
            hand_cricket.main()
            home()
        else:
            home()
    elif opt == 'REFRESH 🌀':
        screen.refresh()
    elif opt == 'POWER OFF 🛑':
        screen.clear()
        design.off()
        screen.clear()
        sys.exit()

##################################################################################
##################################################################################
##################################################################################

if __name__ == '__main__':
    screen.clear()
    design.logo()
    home()
