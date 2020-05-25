##### A S NANDANUNNI #####
#### IG : u.n.n.i._ ######
#### GH : nandan-unni ####

import imp

screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')

contacts = imp.load_source('contacts', './Storage/contacts.py')
notes = imp.load_source('notes', './Storage/notes.py')

calculator = imp.load_source('calculator', './Apps/calculator.py')
hangman = imp.load_source('hangman', './Apps/hangman.py')
cricket = imp.load_source('cricket', './Apps/hand_cricket.py')

settings = imp.load_source('settings', './Settings/settings.py')
date_time = imp.load_source('date_time', './Settings/date_time.py')
key = imp.load_source('key', './Settings/keys.py')


def home():
    screen.clear()
    date_time.timer()
    opt = menu.create_7('CONTACTS 👤', 'NOTES 📚', 'CALCULATOR 📟', 'SETTINGS 🔧', 'GAMES ⚽️', 'REFRESH 🌀', 'POWER OFF 🛑')
    design.create_band(opt)
    if opt == 'CONTACTS 👤':
        subopt = menu.create_5('Add Contact', 'View Contacts', 'Edit Contacts', 'Delete Contacts', 'Back')
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
        subopt = menu.create_3('Hangman', 'Hand Cricket (beta)', 'Back')
        if subopt == 'Hangman':
            hangman.main()
            home()
        elif subopt == 'Hand Cricket (beta)':
            cricket.main()
            home()
        else:
            home()
    
    elif opt == 'REFRESH 🌀':
        home()
    
    elif opt == 'POWER OFF 🛑':
        screen.clear()
        design.off()
        screen.clear()
        exit()

##################################################################################
##################################################################################
##################################################################################

screen.clear()
design.logo()
home()
