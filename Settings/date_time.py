from Settings import keys as key
from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

import datetime
from colorama import Fore, Back, Style

def timer():
    screen.clear()
    print("\n\n")
    clock=datetime.datetime.now()

    if key.get_def('time') == '24':
        if key.get_def('date') == 'number':
            print(Fore.MAGENTA, "\t\t",clock.day,"/",clock.month,"/",clock.year, "\n", Style.RESET_ALL)
            print(Fore.MAGENTA + Style.BRIGHT, "\t\t   ", clock.hour, ":", clock.minute, Style.RESET_ALL)
        else:
            month = design.months[clock.month]
            print(Fore.MAGENTA, "\t\t",clock.day," ",month," ",clock.year, "\n", Style.RESET_ALL)
            print(Fore.MAGENTA + Style.BRIGHT, "\t\t   ", clock.hour, ":", clock.minute, Style.RESET_ALL)
    else:
        if clock.hour > 12:
            hour = clock.hour - 12
            zone = 'pm'
        else:
            hour = clock.hour
            zone = 'am'
        if key.get_def('date') == 'number':
            print(Fore.MAGENTA, "\t\t",clock.day,"/",clock.month,"/",clock.year, "\n", Style.RESET_ALL)
            print(Fore.MAGENTA + Style.BRIGHT, "\t\t  ", hour, ":", clock.minute, zone, Style.RESET_ALL)
        else:
            month = design.months[clock.month]
            print(Fore.MAGENTA, "\t\t",clock.day," ",month," ",clock.year,"\n", Style.RESET_ALL)
            print(Fore.MAGENTA + Style.BRIGHT, "\t\t  ", hour, ":", clock.minute, zone, Style.RESET_ALL)

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


if __name__ == '__main__':
    pass