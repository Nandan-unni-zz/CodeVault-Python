# Rebuilding Hangman

from UI import designs as design
from UI import menu_controller as menu
from UI import screen_controller as screen

import random

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

if __name__ == '__main__':
    pass