
# Main file of the Python 3 program.

import Account as Ac
import Roulette as gamble

print(
    "Hello and Welcome to the game of Roulette! \nThis is a little more simplified and can be played in an interesting sense.")
storeName = input("Please Enter your name: ")

Ac.accountBal(
    input("How much would you like to deposit? "))  # This is where the money is transfered to the file Account.py
print("====================================")
print("Would you like to start the game? \n Yes | No")
stop = input()
while (stop != "No") or (stop != "no"):
    print("====================================")
    a = input(
        "What number would you like to bet on? \nChoose 1-5 for red \nChoose 6-10 for Black \nChoose 0 for Green \nNumber placed: ")  # What the person is placing it on
    if (int(a) <= 10):
        b = input("How much money would you like to bet? ")
        gamble.game(int(a), int(b))
        print("====================================")
        print("Would you like to play again? Yes | No")
        stop = input()
    else:
        print("====================================")
        print("You entered the incorrect number!")







