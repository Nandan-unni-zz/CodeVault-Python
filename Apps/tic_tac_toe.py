import os
from os import system, name
import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')

#format(remote[0], remote[1], remote[2], remote[3], remote[4], remote[5], remote[6], remote[7], remote[8])


def logo(*args):
    design.create_banner(' Tic - Tac - Toe ')
    print('''
         _______________________
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |_______|_______|_______|
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |_______|_______|_______|
        |       |       |       |
        |   {}   |   {}   |   {}   |
        |_______|_______|_______|


'''.format(*args))

def main():
    remote = [1,2,3,4,5,6,7,8,9]
    logo(*remote)
    plr1 = input(('  Player 1, Do you want to be X or O ? '))
    if plr1 == 'X' or plr1 == 'x':
        plr1 = 'X'
        plr2 = 'O'
    else:
        plr1 = 'O'
        plr2 = 'X'
    
    logo(*remote)

    def processor(plr, plno=''):
        final = ''
        chances = ['048', '246', '012', '345', '678', '036', '147', '258']
        pos = input('  Player {} can choose his position : '.format(plno))
        if pos.isnumeric():
            pos = int(pos)
            if pos in [x for x in remote]:
                remote.insert(remote.index(pos), plr)
                remote.remove(pos)
                logo(*remote)
            else:
                print('  Invalid Entry . ! You lost your chance.\n')
        
        else:
            print('  Invalid Entry . ! You lost your chance.\n')
        
        for i in range(len(remote)):
            if remote[i] == plr:
                final = final + str(i)
            else:
                pass
        for chance in chances:
            if set(chance) <= set(final):
                print('  Congrats ! Player {} have won the match.\n'.format(plno))
                input('\t  Home >> ')
                return True
            

    for control in range(1,10):
        if control%2 == 0:
            win = processor(plr1, 1)
            if win:
                return None
        
        else:
            win = processor(plr2, 2)
            if win:
                return None
    
    logo(*remote)
    print('  Draw Match !\n')
    input('\t  Home >> ')
    return None
