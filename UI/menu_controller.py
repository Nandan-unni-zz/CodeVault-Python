def create_1(opt1):
    a1 = int(input('''
  1. {}
  \n
        >> '''.format(opt1)))
    menu_1 = {
        1 : opt1
    }
    return menu_1[a1]



def create_2(opt1, opt2):
    a2 = int(input('''
  1. {}\t\t 2. {}
  \n
        >> '''.format(opt1, opt2)))
    menu_2 = {
        1 : opt1,
        2 : opt2
    }
    return menu_2[a2]



def create_3(opt1, opt2, opt3):
    a3 = int(input('''
  1. {}\t\t 2. {}
      
  3. {}
  \n
        >> '''.format(opt1, opt2, opt3)))
    menu_3 = {
        1 : opt1,
        2 : opt2,
        3 : opt3
    }
    return menu_3[a3]



def create_4(opt1, opt2, opt3, opt4):
    a4 = int(input('''
  1. {}\t\t 2. {}

  3. {}\t\t 4. {}
  \n
        >> '''.format(opt1, opt2, opt3, opt4)))
    menu_4 = {
        1 : opt1,
        2 : opt2,
        3 : opt3,
        4 : opt4
    }
    return menu_4[a4]



def create_5(opt1, opt2, opt3, opt4, opt5):
    a5 = int(input('''
  1. {}\t\t 2. {}

  3. {}\t\t 4. {}

  5. {}
  \n
        >> '''.format(opt1, opt2, opt3, opt4, opt5)))
    menu_5 = {
        1 : opt1,
        2 : opt2,
        3 : opt3,
        4 : opt4,
        5 : opt5
    }
    return menu_5[a5]



def create_6(opt1, opt2, opt3, opt4, opt5, opt6):
    a6 = int(input('''
  1. {}\t\t 2. {}

  3. {}\t\t 4. {}

  5. {}\t\t 6. {}
  \n
        >> '''.format(opt1, opt2, opt3, opt4, opt5, opt6)))
    menu_6 = {
        1 : opt1,
        2 : opt2,
        3 : opt3,
        4 : opt4,
        5 : opt5,
        6 : opt6
    }
    return menu_6[a6]


def create_7(opt1, opt2, opt3, opt4, opt5, opt6, opt7):
    a7 = int(input('''
  1. {}\t\t 2. {}

  3. {}\t\t 4. {}

  5. {}\t\t 6. {}

  7. {}
  \n
         >> '''.format(opt1, opt2, opt3, opt4, opt5, opt6, opt7)))
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