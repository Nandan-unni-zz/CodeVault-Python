##### A S NANDANUNNI #####
#### IG : u.n.n.i._ ######
#### GH : nandan-unni ####

import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')
contacts = imp.load_source('contacts', './Storage/contacts.py')

def home():
    screen.clear()
    design.timer()
    opt = menu.create_4('CONTACTS', 'NOTES', 'REFRESH', 'POWER OFF')
    if opt == 'CONTACTS':
        screen.clear()
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
        home()
    elif opt == 'REFRESH':
        home()
    
    elif opt == 'POWER OFF':
        screen.clear()
        design.off()
        screen.clear()
        exit()
    
screen.clear()
design.logo()
home()