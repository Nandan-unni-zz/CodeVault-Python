import os
from os import system, name

def clear():
    os.system('cls' if os.name=='nt' else 'clear')