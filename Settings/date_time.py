import datetime
import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')
key = imp.load_source('key', './Settings/keys.py')

def timer():
    screen.clear()
    print("\n\n")
    clock=datetime.datetime.now()

    if key.get_def('time') == '24':
        if key.get_def('date') == 'number':
            print("\t\t",clock.day,"/",clock.month,"/",clock.year,"/n")
            print("\t\t   ",clock.hour,":",clock.minute)
        else:
            month = design.months[clock.month]
            print("\t\t",clock.day," ",month," ",clock.year, "/n")
            print("\t\t   ",clock.hour,":",clock.minute)
    else:
        if clock.hour > 12:
            hour = clock.hour - 12
            zone = 'pm'
        else:
            zone = 'am'
        if key.get_def('date') == 'number':
            print("\t\t",clock.day,"/",clock.month,"/",clock.year, "/n")
            print("\t\t  ",hour,":",clock.minute, zone)
        else:
            month = design.months[clock.month]
            print("\t\t",clock.day," ",month," ",clock.year,"\n")
            print("\t\t  ",hour,":",clock.minute, zone)

    print('\n\n')

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