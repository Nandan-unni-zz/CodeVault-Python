import datetime
import time
import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
key = imp.load_source('key', './Settings/keys.py')

def logo():
    print(''' 
        
            P R O T O N 

    ''')
    time.sleep(0.5)


def off():
    print("\n\n")
    print("\t      **      ")
    print("\t     /  \     ")
    print("\t*---*----*---*")
    print("\t \ /      \ / ")
    print("\t  * PROTON *  ")
    print("\t / \      / \ ")
    print("\t*---*----*---*")
    print("\t     \  /     ")
    print("\t      **      ")
    time.sleep(0.5)


def timer():
    screen.clear()
    print("\n\n")
    clock=datetime.datetime.now()

    if key.get_def('time') == '24':
        if key.get_def('date') == 'number':
            print("\t\t",clock.day,"/",clock.month,"/",clock.year)
            print("\t\t   ",clock.hour,":",clock.minute)
        else:
            month = key.months[clock.month]
            print("\t\t",clock.day," ",month," ",clock.year)
            print("\t\t   ",clock.hour,":",clock.minute)
    else:
        if clock.hour > 12:
            hour = clock.hour - 12
            zone = 'pm'
        else:
            zone = 'am'
        if key.get_def('date') == 'number':
            print("\t\t",clock.day,"/",clock.month,"/",clock.year)
            print("\t\t  ",hour,":",clock.minute, zone)
        else:
            month = key.months[clock.month]
            print("\t\t",clock.day," ",month," ",clock.year)
            print("\t\t  ",hour,":",clock.minute, zone)

    print('\n')


def create_logo(label):
    screen.clear()
    if len(label) <= 16:
        title = ' '.join(label)
    else:
        title = label
    dsgn1 = '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
    dsgn2 = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
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

    print('''\n\n
{}
{}
{}
{}
{}
    '''.format(dsgn1, dsgn2, dsgn3, dsgn2, dsgn1))


def create_banner(label):
    screen.clear()
    if len(label) <= 16:
        title = ' '.join(label)
    else:
        title = label
    dsgn1 = '*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*'
    dsgn2 = '.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.'
    dslen = len(dsgn2)
    ttlen = len(title)
    rem = int((dslen - ttlen)/2)
    for i in range(0, dslen):
        if (i == rem):
            for j in range(ttlen):
                rem = rem + 1
                dsgn2 = dsgn2[:rem] + title[j] + dsgn2[rem+1:]
            break

    print('''\n\n
{}
{}
{}
    '''.format(dsgn1, dsgn2, dsgn1))


def create_band(label):
    screen.clear()
    if len(label) <= 16:
        title = ' '.join(label)
    else:
        title = label
    
    dsgn1 = '>>>>>  '
    dsgn2 = '  <<<<<'
    dsgn = dsgn1 + title + dsgn2
    totlen = len(dsgn) + len(dsgn1) + len(dsgn2)
    print('\n')
    for i in range(50 - totlen):
        print(' ', end="")
    print(dsgn, '\n')