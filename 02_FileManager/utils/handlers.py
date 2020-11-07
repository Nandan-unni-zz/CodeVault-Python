from colorama import Fore, Style
from .designer import signal, message

def dirmenu(options = [''], index = 1):
    print("\b")
    for i in range(len(options)):
        if i % 2 == 0:
            print(Fore.BLUE, Style.BRIGHT, index, "\b.", end="")
            print(Style.RESET_ALL, "\b", options[i], end="")
            for i in range(30 - len(options[i])): print(end=" ")
            index = index + 1
        else:
            print(Fore.BLUE, Style.BRIGHT, index, "\b.", end="")
            print(Style.RESET_ALL, "\b", options[i])
            index = index + 1
    print("\n")

def filemenu(options = ['']):
    print("\b")
    for i in range(len(options)):
        signal(f"{i+1}.")
        message(f"\b\b{options[i]}\t")
    print("\n")

def dev():
    pdb.set_trace()
