from Settings import keys as key
from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

import datetime
from colorama import Fore, Style

def timer():
    screen.clear()
    clock = datetime.datetime.now()

    def disp(dd, mm, yy, day, hr, mn, zn):
        date = dd + ' ' + mm + ' ' + yy + ', ' + day
        time = hr + ' : ' + mn + ' ' + zn
        print('\n', Fore.RED + Style.BRIGHT)
        for x in range(51): print('_', end='')
        print('\n', Style.RESET_ALL)
        print(Fore.MAGENTA, date.center(50, ' '), "\n", Style.RESET_ALL)
        print(Fore.MAGENTA + Style.BRIGHT, time.center(50, ' '), Fore.RED)
        for x in range(51): print('_', end='')
        print('', Style.RESET_ALL)
        del x, date, time

    if key.get_def('time') == '24':
        if key.get_def('date') == 'number':
            disp(clock.strftime('%d'), clock.strftime('%m'), clock.strftime('%Y'), clock.strftime('%A'),
                 clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%p'))
        else:
            disp(clock.strftime('%d'), clock.strftime('%b'), clock.strftime('%Y'), clock.strftime('%A'),
                 clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%p'))
    else:
        if key.get_def('date') == 'number':
            disp(clock.strftime('%d'), clock.strftime('%b'), clock.strftime('%Y'), clock.strftime('%A'),
                 clock.strftime('%l'), clock.strftime('%M'), clock.strftime('%p'))
        else:
            disp(clock.strftime('%d'), clock.strftime('%m'), clock.strftime('%Y'), clock.strftime('%A'),
                 clock.strftime('%l'), clock.strftime('%M'), clock.strftime('%p'))

    del clock
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