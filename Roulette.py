import math
import random
import Account as win


# random.randint(1,10)
def game(num, money):
    number = int(num)
    gen = int(random.randint(0, 10))
    print("====================================")
    print("The roulette landed on ", gen)
    if (gen == 0) and (number == 0):
        jackpot = 14 * money
        print("====================================")
        print("You won ", jackpot, "from green!")
        print(number, "is your number")
        win.winBal(jackpot)
        pass
    elif (gen > 0 and gen < 6) and (number > 0 and number < 6):
        print("====================================")
        print("You won", money, "from red!")
        print(number, "is your number")
        win.winBal(money)

    else:
        print("====================================")
        print("You lost ", money, "!")
        win.winBal(-1 * money)

