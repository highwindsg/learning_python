#try to refer to ex35.py
#create functions for different choices
#and within each choice functions, have their own mini story line.
from sys import exit

print("\n")
print("You are born to this world and are now presented with two choices.")
print("Would you choose the Book or the Sword?")
print("1. Book")
print("2. Sword")
print("[Press 1 or 2 and press Enter]")

choice = input("> ")

if choice == "1":
    print("There are the two different classes of discipline.")
    print("Pick one discipline.")
    print("1. Warlock")
    print("2. Cleric")
    print("[Press 1 or 2 and press Enter]")

    classes = input("> ")

    if classes == "1":
        print("House of Slytherin you go!")
    elif classes == "2":
        print("House of Gryffindor you go!")
    else:
        print(f"Well ... not choosing {classes} any I see. Perhaps you wish to reconsider.")

elif choice == "2":
    print("There are two types of swordmen discipline to train in.")
    print("Pick one type of training.")
    print("1. Ranger")
    print("2. Knight")
    print("[Press 1 or 2 and press Enter]")

    swordsmen = input("> ")

    if swordsmen == "1":
        print("The land of Rohan you go!")
    elif swordsmen == "2":
        print("The castle of Minas Tirith you go!")
    else:
        print("Well ... not choosing {swordsmen} any I see. Perhaps you wish to reconsider.")

else:
    print("Perhaps you wish you were never born, I think.")

