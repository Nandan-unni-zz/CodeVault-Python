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
    random_pos = random.randint(0,5)
    ans = words[random_pos]
    qn = words[random_pos]
    word_len = len(ans)
    for i in range(1, word_len + 1):
        if i % 3 != 0:
            qn = qn.replace(qn[i-1], str(i), 1)
    health = 5
    found = False
    while health > 0:
        title()
        print("\n\n\t", end="")
        for i in range(word_len):
            if qn[i].isdigit() == True:
                print("__", end=" ")
            else:
                print(qn[i], end=" ")
        print("\n\n\tLife : ", health)
        guess_letter = input("\n\n\tGuess a letter : ")
        found = False
        for i in range(word_len):
            if guess_letter == ans[i]:
                found = True
                qn = qn.replace(qn[i], ans[i], 1)
        if found:
            if qn == ans:
                victory()
                opt = int(input('1. Play Again \t 2. Quit \n\t : '))
                if opt == 1:
                    main()
                else:
                    return None
        else:
            health = health - 1
            print("\n\n\tThe word doesn't contain", guess_letter)
            pause()
        title()
        print("\n\n\t",end="")
        for i in range(word_len):
            if qn[i].isdigit():
                print("__", end=" ")
            else:
                print(qn[i], end=" ")
        print("\n\n\tLife : ", health)
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
                health = health - 1
                print("\n\n\tWrong..!\n\n\t  ", health, " life remaining.")
                pause()
    if health == 0:
        print(' BETTER LUCK NEXT TIME ')
        opt = int(input('1. Play Again \t 2. Back \n\t : '))
        if opt == 1:
            main()
        else:
            return None

if __name__ == "__main__":
    main()
