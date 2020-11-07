import random
import time

def msg(m):
    for i in range(len(m) + 4):
        print("_", end="")
    print(f"\n\n  {m}  ")
    for i in range(len(m) + 4):
        print("_", end="")

def end(init, now):
    if init == now:
        print("You have no gain and no loss.")
    elif init > now:
        print(f"\nYou lost {init-now}")
    else:
        print(f"\nYou gained {now-init}")

print("\nYour balance will be the double of what you bet. ")
bet_plr = int(input("Enter the bet amount : $ "))
bet_dlr = 100 * (random.randint(5, 10))
if bet_plr > 1000:
    print("Max amount is 1000")
    bet_plr = 1000
elif bet_plr < 500:
    print("Min amount is 500")
    bet_plr = 500

init_plr = amt_plr = 2 * bet_plr
amt_dlr = 2 * bet_dlr
print(f"\n\nPlayer Bet Amount : $ {bet_plr}")
print(f"Dealer Bet Amount : $ {bet_dlr}")

while True:
    num_plr = int(input("\nEnter your number (1-8) : "))
    if num_plr > 8:
        print("Top number is 8")
        num_plr = 8
    elif num_plr < 1:
        print("Lowest number is 1")
        num_plr = 1

    print(f"\n\nPlayer's Number : {num_plr}")

    while True:
        num_dlr = random.randint(1, 8)
        if num_dlr != num_plr:
            break

    print(f"Dealer Number : {num_dlr}")

    print("\nRolling . . ", end="")
    print(".")
    time.sleep(2)
    num_luck = random.randint(1, 8)
    print(f"\nDrawn Number : {num_luck}")
    if num_plr == num_luck:
        amt_plr += bet_dlr
        amt_dlr -= bet_dlr
        msg("PLAYER WON !")
        if amt_dlr <= 0:
            print("\nDealer lost all his money", end="")
            end(init_plr, amt_plr)
            break
    elif num_dlr == num_luck:
        amt_plr -= bet_plr
        amt_dlr += bet_dlr
        msg("DEALER WON !")
        if amt_plr <= 0:
            print("\nYour balance is 0.", end="")
            end(init_plr, 0)
            break
    else:
        msg("DRAW !")

    print(f"\n\nPlayer's Balance : $ {amt_plr}")
    print(f"Dealer's Balance : $ {amt_dlr}")
    cont = int(input("\n1. Continue \t 2. Quit \t : "))
    print("___________________________________________________")
    if cont == 2:
        end(init_plr, amt_plr)
        break
