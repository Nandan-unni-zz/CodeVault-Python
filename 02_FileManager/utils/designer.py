import os
from colorama import Fore, Style

def logo(text):
    clear()
    text = text.upper()
    text = text.center(94, " ")
    print(Fore.BLUE, Style.BRIGHT, end="\b")
    for i in range(100): print("*", end="")
    print("\n**", Fore.GREEN, text, Fore.BLUE, end="\b**\n")
    for i in range(100): print("*", end="")
    print(Style.RESET_ALL, "\n")
    # return input()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal(text = ""):
    print(Fore.BLUE, Style.BRIGHT, text, Style.RESET_ALL, end="")

def message(text = ""):
    print(Fore.GREEN, Style.BRIGHT, text, Style.RESET_ALL, end="")

def warning(text = ""):
    print(Fore.YELLOW, Style.BRIGHT, text, Style.RESET_ALL, end="")

def alert(text = ""):
    print(Fore.RED, Style.BRIGHT, text, Style.RESET_ALL, end="")

if __name__ == "__main__":
    clear()
    logo("Loreme Ipsum")
    signal("Lorem Ipsum")
    message("Lorem Ipsum")
    warning("Lorem Ipsum")
    alert("Lorem Ipsum")
    menu(["Lorem", "Ipsum", "Lorem", "Ipsum", "Lorem"])
    toolbar(["Lorem", "Ipsum", "Lorem", "Ipsum", "Lorem"])
