from colorama import Fore, Back, Style


def create_2(opt1, opt2):

    menu_2 = {
        1 : opt1,
        2 : opt2
    }

    print(Fore.RED,
            ' 1.', Style.RESET_ALL, '{}\t\t'.format(opt1), Fore.RED, '2.', Style.RESET_ALL, '{}\n\n'.format(opt2), Fore.RED,
            Fore.MAGENTA, '\n\n\n\t>> ', end="")
    a2 = input()
    print(Style.RESET_ALL)

    if a2.isnumeric() and int(a2) in menu_2.keys():
        return menu_2[int(a2)]
    else:
        return opt2



def create_3(opt1, opt2, opt3):

    menu_3 = {
        1 : opt1,
        2 : opt2,
        3 : opt3
    }

    print(Fore.RED,
            ' 1.', Style.RESET_ALL, '{}\t\t'.format(opt1), Fore.RED, '2.', Style.RESET_ALL, '{}\n\n'.format(opt2), Fore.RED,
            '3.', Style.RESET_ALL, '{}'.format(opt3), Fore.MAGENTA, '\n\n\n\t>> ', end="")
    a3 = input()
    print(Style.RESET_ALL)

    if a3.isnumeric() and int(a3) in menu_3.keys():
        return menu_3[int(a3)]
    else:
        return opt3



def create_4(opt1, opt2, opt3, opt4):

    menu_4 = {
        1 : opt1,
        2 : opt2,
        3 : opt3,
        4 : opt4
    }

    print(Fore.RED,
            ' 1.', Style.RESET_ALL, '{}\t\t\t'.format(opt1), Fore.RED, '2.', Style.RESET_ALL, '{}\n\n'.format(opt2), Fore.RED,
            '3.', Style.RESET_ALL, '{}\t\t'.format(opt3), Fore.RED, '4.', Style.RESET_ALL, '{}\n\n'.format(opt4), Fore.RED,
            Fore.MAGENTA, '\n\n\n\t>> ', end="")
    a4 = input()
    print(Style.RESET_ALL)

    if a4.isnumeric() and int(a4) in menu_4.keys():
        return menu_4[int(a4)]
    else:
        return opt4


def create_5(opt1, opt2, opt3, opt4, opt5):

    menu_5 = {
        1 : opt1,
        2 : opt2,
        3 : opt3,
        4 : opt4,
        5 : opt5
    }

    print(Fore.RED,
            ' 1.', Style.RESET_ALL, '{}\t\t'.format(opt1), Fore.RED, '2.', Style.RESET_ALL, '{}\n\n'.format(opt2), Fore.RED,
            '3.', Style.RESET_ALL, '{}\t\t'.format(opt3), Fore.RED, '4.', Style.RESET_ALL, '{}\n\n'.format(opt4), Fore.RED,
            '5.', Style.RESET_ALL, '{}'.format(opt5), Fore.MAGENTA, '\n\n\n\t>> ', end="")
    a5 = input()
    print(Style.RESET_ALL)

    if a5.isnumeric() and int(a5) in menu_5.keys():
        return menu_5[int(a5)]
    else:
        return opt5


def create_6(opt1, opt2, opt3, opt4, opt5, opt6):

    menu_6 = {
        1 : opt1,
        2 : opt2,
        3 : opt3,
        4 : opt4,
        5 : opt5,
        6 : opt6
    }

    print(Fore.RED,
            ' 1.', Style.RESET_ALL, '{}\t\t'.format(opt1), Fore.RED, '2.', Style.RESET_ALL, '{}\n\n'.format(opt2), Fore.RED,
            '3.', Style.RESET_ALL, '{}\t\t'.format(opt3), Fore.RED, '4.', Style.RESET_ALL, '{}\n\n'.format(opt4), Fore.RED,
            '5.', Style.RESET_ALL, '{}\t\t\t'.format(opt5), Fore.RED, '6.', Style.RESET_ALL, '{}\n\n'.format(opt6), Fore.RED,
            Fore.MAGENTA, '\n\n\n\t>> ', end="")
    a6 = input()
    print(Style.RESET_ALL)

    if a6.isnumeric() and int(a6) in menu_6.keys():
        return menu_6[int(a6)]
    else:
        return opt6

def create_7(opt1, opt2, opt3, opt4, opt5, opt6, opt7):
    
    menu_7 = {
        1 : opt1,
        2 : opt2,
        3 : opt3,
        4 : opt4,
        5 : opt5,
        6 : opt6,
        7 : opt7
    }

    print(Fore.RED,
            ' 1.', Style.RESET_ALL, '{}\t\t'.format(opt1), Fore.RED, '2.', Style.RESET_ALL, '{}\n\n'.format(opt2), Fore.RED,
            '3.', Style.RESET_ALL, '{}\t\t'.format(opt3), Fore.RED, '4.', Style.RESET_ALL, '{}\n\n'.format(opt4), Fore.RED,
            '5.', Style.RESET_ALL, '{}\t\t\t'.format(opt5), Fore.RED, '6.', Style.RESET_ALL, '{}\n\n'.format(opt6), Fore.RED,
            '7.', Style.RESET_ALL, '{}'.format(opt7), Fore.MAGENTA, '\n\n\n\t>> ', end="")

    a7 = input()
    print(Style.RESET_ALL)
    if a7.isnumeric() and int(a7) in menu_7.keys():
        return menu_7[int(a7)]
    else:
        return opt6


if __name__ == '__main__':
    pass