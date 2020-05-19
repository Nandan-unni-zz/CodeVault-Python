##### A S NANDANUNNI #####
#### IG : u.n.n.i._ ######
#### GH : nandan-unni ####

import imp

screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')

contacts = imp.load_source('contacts', './Storage/contacts.py')
notes = imp.load_source('notes', './Storage/notes.py')

hangman = imp.load_source('hangman', './Apps/hangman.py')
calculator = imp.load_source('calculator', './Apps/calculator.py')

settings = imp.load_source('settings', './Settings/settings.py')
key = imp.load_source('key', './Settings/keys.py')


def home():
    screen.clear()
    design.timer()
    opt = menu.create_7('CONTACTS', 'NOTES', 'CALCULATOR', 'SETTINGS', 'GAMES', 'REFRESH', 'POWER OFF')
    design.create_band(opt)
    if opt == 'CONTACTS':
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
    
    elif opt == 'NOTES':
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

    elif opt == 'CALCULATOR':
        calculator.main()
        home()

    elif opt == 'SETTINGS':
        subopt = menu.create_4('Date', 'Time', 'Factory Reset', 'Back')
        if subopt == 'Time':
            settings.time_format()
            home()
        
        elif subopt == 'Date':
            settings.date_format()
            home()
        
        elif subopt == 'Factory Reset':
            settings.factory_reset()
            home()
        else:
            home()
    
    elif opt == 'GAMES':
        subopt = menu.create_2('Hangman', 'Back')
        if subopt == 'Hangman':
            hangman.main()
            home()
        else:
            home()
    
    elif opt == 'REFRESH':
        home()
    
    elif opt == 'POWER OFF':
        screen.clear()
        design.off()
        screen.clear()
        exit()

##################################################################################
##################################################################################

screen.clear()
design.logo()
home()