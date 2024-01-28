"""
ATM application with deposit, transfer, withdraw functions
"""

from pyfiglet import Figlet
from ATM import *

# WELCOME SCREEN

fig = Figlet(font="isometric1")
print(fig.renderText("ATM"))

PLAY_AGAIN = True

while PLAY_AGAIN:

    print("\n>>> MENU <<<\n")
    print("Enter '1' to VIEW your CHECKING account balance")
    print("Enter '2' to VIEW your SAVINGS account balance")
    print("Enter '3' to WITHDRAW funds from your CHECKING account")
    print("Enter '4' to DEPOSIT funds into your CHECKING account")
    print("Enter '5' to WITHDRAW funds from your SAVINGS account")
    print("Enter '6' to DEPOSIT funds into your SAVINGS account")
    print(
        "Enter '7' to TRANSFER funds from your CHECKING account into your SAVINGS account"
    )
    print(
        "Enter '8' to TRANSFER funds from your SAVINGS account into your CHECKING account\n"
    )

    menu_choice = int(input("Enter option: "))  # APP CHOICE

    match menu_choice:  # APP LOGIC
        case 1:
            ATM.checking_balance()
        case 2:
            ATM.savings_balance()
        case 3:
            ATM.withdraw_checking()
        case 4:
            ATM.deposit_checking()
        case 5:
            ATM.withdraw_savings()
        case 6:
            ATM.deposit_savings()
        case 7:
            ATM.checking_to_savings()
        case 8:
            ATM.savings_to_checking()

    replay_choice = input("\nTry another translation? Enter Y/N...: ")  # APP REPLAY

    PLAY_AGAIN = bool(replay_choice.upper() == "Y")

print("\nThanks! See you again next time!")  # APP END
