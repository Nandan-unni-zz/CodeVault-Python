from colorama import Fore, Back, Style


def create_1(opt1):
    a1 = input('''
  1. {}
  \n
        >> '''.format(opt1))
    if a1.isnumeric():
        a1 = int(a1)
        menu_1 = {
            1 : opt1
        }
        return menu_1[a1]
    else:
        return opt1



def create_2(opt1, opt2):
    a2 = input('''
  1. {}\t\t2. {}
  \n
        >> '''.format(opt1, opt2))
    if a2.isnumeric():
        a2 = int(a2)
        menu_2 = {
            1 : opt1,
            2 : opt2
        }
        return menu_2[a2]
    else:
        return opt2



def create_3(opt1, opt2, opt3):
    a3 = input('''
  1. {}\t\t2. {}
      
  3. {}
  \n
        >> '''.format(opt1, opt2, opt3))
    if a3.isnumeric():
        a3 = int(a3)
        menu_3 = {
            1 : opt1,
            2 : opt2,
            3 : opt3
        }
        return menu_3[a3]
    else:
        return opt3



def create_4(opt1, opt2, opt3, opt4):
    a4 = input('''
  1. {}\t\t2. {}

  3. {}\t\t4. {}
  \n
        >> '''.format(opt1, opt2, opt3, opt4))
    if a4.isnumeric():
        a4 = int(a4)
        menu_4 = {
            1 : opt1,
            2 : opt2,
            3 : opt3,
            4 : opt4
        }
        return menu_4[a4]
    else:
        return opt4


def create_5(opt1, opt2, opt3, opt4, opt5):
    a5 = input('''
  1. {}\t\t2. {}

  3. {}\t\t4. {}

  5. {}
  \n
        >> '''.format(opt1, opt2, opt3, opt4, opt5))
    if a5.isnumeric():
        a5 = int(a5)
        menu_5 = {
            1 : opt1,
            2 : opt2,
            3 : opt3,
            4 : opt4,
            5 : opt5
        }
        return menu_5[a5]
    else:
        return opt5


def create_6(opt1, opt2, opt3, opt4, opt5, opt6):
    a6 = input('''
  1. {}\t\t2. {}

  3. {}\t\t4. {}

  5. {}\t\t6. {}
  \n
        >> '''.format(opt1, opt2, opt3, opt4, opt5, opt6))
    if a6.isnumeric():
        a6 = int(a6)
        menu_6 = {
            1 : opt1,
            2 : opt2,
            3 : opt3,
            4 : opt4,
            5 : opt5,
            6 : opt6
        }
        return menu_6[a6]
    else:
        return opt6

def create_7(opt1, opt2, opt3, opt4, opt5, opt6, opt7):
    print(Fore.RED,
            ' 1.', Style.RESET_ALL, '{}\t\t'.format(opt1), Fore.RED, '2.', Style.RESET_ALL, '{}\n\n'.format(opt2), Fore.RED,
            '3.', Style.RESET_ALL, '{}\t\t'.format(opt3), Fore.RED, '4.', Style.RESET_ALL, '{}\n\n'.format(opt4), Fore.RED,
            '5.', Style.RESET_ALL, '{}\t\t\t'.format(opt5), Fore.RED, '6.', Style.RESET_ALL, '{}\n\n'.format(opt6), Fore.RED,
            '7.', Style.RESET_ALL, '{}'.format(opt7), Fore.MAGENTA, '\n\n\n\t>> ', end="")

    a7 = input()
    print(Style.RESET_ALL)
    if a7.isnumeric():
        a7 = int(a7)
        menu_7 = {
            1 : opt1,
            2 : opt2,
            3 : opt3,
            4 : opt4,
            5 : opt5,
            6 : opt6,
            7 : opt7
        }
        return menu_7[a7]
    else:
        return opt6


if __name__ == '__main__':
    pass