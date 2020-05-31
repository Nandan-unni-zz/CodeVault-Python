import random
import imp
screen = imp.load_source('screen', './UI/screen_controller.py')
menu = imp.load_source('menu', './UI/menu_controller.py')
design = imp.load_source('design', './UI/designs.py')

def main():
    def title():
        design.create_logo(' HANGMAN ')
        print("\n\n\t\tGuess the Word..!!!")

    def victory():
        screen.clear()
        print("\n\n\tThe word is",ans)
        design.create_banner(' VICTORY ')

    def pause():
        input("\n\t   Press Enter to continue...")

    words=["apple","orange","grapes","banana","pineapple","jackfruit"]
    #     ["__p__","__a__e","__a__s","__n__a","__n__p__e","__c__r__t"]
    a=random.randint(0,5)
    ans=words[a]
    guess=words[a]
    del a
    l=len(ans)
    for i in range(1,l+1):
        if i%3!=0:
            guess=guess.replace(guess[i-1],str(i),1)
    h=5
    f=0
    while h>0:
        title()
        print("\n\n\t",end="")
        for i in range(l):
            if guess[i].isdigit()==True:
                print("__",end=" ")
            else:
                print(guess[i],end=" ")
        print("\n\n\tLife : ",h)
        z=input("\n\n\tGuess a letter : ")
        f=0
        for i in range(l):
            if z==ans[i]:
                f=f+1
                guess=guess.replace(guess[i],ans[i],1)
        if f>0:
            if guess==ans:
                victory()
                opt = menu.create_2('Play Again', 'Back')
                if opt == 'Play Again':
                    main()
                else:
                    return None
        else:
            h=h-1
            print("\n\n\tThe word doesn't contain",z)
            pause()
        title()
        print("\n\n\t",end="")
        for i in range(l):
            if guess[i].isdigit()==True:
                print("__",end=" ")
            else:
                print(guess[i],end=" ")
        print("\n\n\tLife : ",h)
        y=input("\n\n\tDid you get the word ? (y/n) : ")
        if y=='y':
            temp=str(input("\n\t    Your Answer : "))
            if temp==ans:
                victory()
                opt = menu.create_2('Play Again', 'Back')
                if opt == 'Play Again':
                    main()
                else:
                    return None
            else:
                h=h-1
                print("\n\n Wrong..!\n",h," life remaining.")
                pause()
    if h==0:
        design.create_banner(' BETTER LUCK NEXT TIME ')
        opt = menu.create_2('Play Again', 'Back')
        if opt == 'Play Again':
            main()
        else:
            return None