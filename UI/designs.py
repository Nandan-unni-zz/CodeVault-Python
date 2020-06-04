import datetime
import time
from colorama import Fore, Back, Style

from UI import menu_controller as menu
from UI import screen_controller as screen

def logo():
    print(Fore.RED + Style.BRIGHT, ''' 
        
                P R O T O N

    ''', Style.RESET_ALL)
    time.sleep(0.5)


def off():
    print("\n\n")
    print(Fore.MAGENTA, "\t      **      ")
    print("\t     /  \     ")
    print("\t*---*----*---*")
    print("\t \ /      \ / ")
    print("\t  * " + Fore.RED + Style.BRIGHT + "PROTON" + Style.RESET_ALL + Fore.MAGENTA, " *  ")
    print("\t / \      / \ ")
    print("\t*---*----*---*")
    print("\t     \  /     ")
    print("\t      **      ", Style.RESET_ALL)
    time.sleep(0.5)


def create_logo(label):
    screen.clear()
    if len(label) <= 16:
        title = ' '.join(label)
    else:
        title = label
    dsgn1 = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
    dsgn2 = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
    dsgn3 = dsgn1
    dslen = len(dsgn3)
    ttlen = len(title)
    rem = int((dslen - ttlen)/2)
    for i in range(0, dslen):
        if (i == rem):
            for j in range(ttlen):
                rem = rem + 1
                dsgn3 = dsgn3[:rem] + title[j] + dsgn3[rem+1:]
            break

    print(Fore.MAGENTA, '\n\n\n{}'.format(dsgn1), Style.RESET_ALL,
        Fore.MAGENTA, '\n{}'.format(dsgn2), Style.RESET_ALL,
        Fore.RED, '\n{}'.format(dsgn3), Style.RESET_ALL,
        Fore.MAGENTA, '\n{}'.format(dsgn2), Style.RESET_ALL,
        Fore.MAGENTA, '\n{}\n'.format(dsgn1), Style.RESET_ALL )


def create_banner(label):
    screen.clear()
    if len(label) <= 15:
        title = ' '.join(label)
    else:
        title = label
    dsgn1 = '*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*. '
    dsgn2 = '.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*'
    dslen = len(dsgn2)
    ttlen = len(title)
    rem = int((dslen - ttlen)/2)
    for i in range(0, dslen):
        if (i == rem):
            for j in range(ttlen):
                rem = rem + 1
                dsgn2 = dsgn2[:rem] + title[j] + dsgn2[rem+1:]
            break

    print(Fore.MAGENTA, '\n\n\n{}'.format(dsgn1), Style.RESET_ALL,
        Fore.RED, '\n{}'.format(dsgn2), Style.RESET_ALL,
        Fore.MAGENTA, '\n{}\n'.format(dsgn1), Style.RESET_ALL
    )


def create_band(label):
    screen.clear()
    if len(label) <= 16:
        dsgn = ' '.join(label)
    else:
        dsgn = label
    
    print('\n', Fore.RED, Style.BRIGHT)
    for x in range(51): print('_', end='')
    print('\n', Style.RESET_ALL)
    print(Fore.MAGENTA, Style.BRIGHT, dsgn.center(50, ' '), Fore.RED)
    for x in range(51): print('_', end='')
    print('\n\n', Style.RESET_ALL)
    del x

if __name__ == '__main__':
    pass