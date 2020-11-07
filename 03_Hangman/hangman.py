import random
import os

def main():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def title():
        clear()
        print('\n\t\tHANGMAN\n')
        print("\n\n\t\tGuess the Word..!!!")

    def victory():
        clear()
        print("\n\n\tThe word is", ans)
        print('\n\t\tVICTORY\n')

    def pause():
        input("\n\t   Press Enter to continue...")

    words = ["apple", "orange", "grapes", "banana", "pineapple", "jackfruit"]
    #     ["__p__","__a__e","__a__s","__n__a","__n__p__e","__c__r__t"]
    a = random.randint(0,5)
    ans = words[a]
    guess = words[a]
    del a
    l = len(ans)
    for i in range(1, l+1):
        if i % 3 != 0:
            guess = guess.replace(guess[i-1], str(i), 1)
    h = 5
    f = 0
    while h > 0:
        title()
        print("\n\n\t", end="")
        for i in range(l):
            if guess[i].isdigit() == True:
                print("__", end=" ")
            else:
                print(guess[i], end=" ")
        print("\n\n\tLife : ", h)
        z = input("\n\n\tGuess a letter : ")
        f = 0
        for i in range(l):
            if z == ans[i]:
                f = f+1
                guess = guess.replace(guess[i], ans[i], 1)
        if f > 0:
            if guess == ans:
                victory()
                opt = int(input('1. Play Again \t 2. Quit \n\t : '))
                if opt == 1:
                    main()
                else:
                    return None
        else:
            h = h-1
            print("\n\n\tThe word doesn't contain", z)
            pause()
        title()
        print("\n\n\t",end="")
        for i in range(l):
            if guess[i].isdigit() == True:
                print("__", end=" ")
            else:
                print(guess[i], end=" ")
        print("\n\n\tLife : ", h)
        y = input("\n\n\tDid you get the word ? (y/n) : ")
        if y == 'y':
            temp = str(input("\n\t    Your Answer : "))
            if temp == ans:
                victory()
                opt = int(input('1. Play Again \t 2. Quit \n\t : '))
                if opt == 'Play Again':
                    main()
                else:
                    return None
            else:
                h = h-1
                print("\n\n\tWrong..!\n\n\t  ", h, " life remaining.")
                pause()
    if h == 0:
        print(' BETTER LUCK NEXT TIME ')
        opt = int(input('1. Play Again \t 2. Back \n\t : '))
        if opt == 1:
            main()
        else:
            return None

if __name__ == "__main__":
    main()
