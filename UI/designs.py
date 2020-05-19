import datetime
import time
import imp
screen = imp.load_source('screen', './UI/screen_controller.py')

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
    print("\t\t",clock.day,"/",clock.month,"/",clock.year)
    print("\t\t   ",clock.hour,":",clock.minute)
    print('\n')

timer()