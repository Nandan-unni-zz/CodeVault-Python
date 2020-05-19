import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')

def main():
    design.create_logo(' CALCULATOR ')
    a = float(input("\nEnter first number: "))
    b = input("\nEnter the operator: ")
    c = float(input("\nEnter second number: "))
    f = 0
    if b == '+':
        d = a + c
    elif b == '-':
        d = a - c
    elif b == '*':
        d = a * c
    elif (b == '/') or (b == '\\'):
        if c == 0:
            print("\ndivision by 0 is not possible..!")
            f = 1
        else:
            d = a / c
    elif b == '^':
        d = a ** c
    elif b == '%':
        d = a % c
    else:
        print("\nInvalid Operator")
        f=1
    if f == 0:
        print("\n",a,b,c,"=",d)
    opt = menu.create_2('Continue', 'Back')
    if opt == 'Continue':
        main()
    else:
        return None