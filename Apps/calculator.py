from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

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

if __name__ == '__main__':
    pass