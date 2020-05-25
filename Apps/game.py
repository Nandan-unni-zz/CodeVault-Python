# Rebuilding Hangman

import random
import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')

def main():
    print('\n\tLoaded..!\n\n')
    life = 5
    words = [
        'australia', 'greenland', 'switzerland', 'india', 'pakistan',
        'apple', 'mango', 'banana',
        'angry', 'selfish'
        ]
    a = random.randint(0,len(words)-1)
    ans = words[a]
    del a
    print(ans)

    life = 5
    length = len()
    for i in range(length):
        print(i)
        model = life
    
    print(model)

screen.clear()
main()