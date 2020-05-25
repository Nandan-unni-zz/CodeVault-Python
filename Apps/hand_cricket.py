import random
import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')


def twenty():
    screen.clear()
    total_score = random.randint(21, 30)
    total_over = 5
    score = 0
    wicket = 2
    design.create_banner(' 20 - 20 ')
    print('''

                SCOREBOARD

    TARGET
    Runs : {} \t Overs : {} \t Wickets : {}

    SCORE
    Runs : {} \t Overs : {} \t Wickets : {}


    NEED {} runs from {} balls to WIN
    ''')
'''
def test():
    screen.clear()
    print('Test Cricket')

def world():
    screen.clear()
    print('World Cup')
'''
def main():
    screen.clear()
    opt = menu.create_4('20 - 20', 'Test Cricket', 'Wolrd Cup', 'Exit')

    if opt == '20 - 20':
        twenty()
        '''
    elif opt == 'Test Cricket':
        test()

    elif opt == 'World Cup':
        world()
        '''
    else:
        exit()

