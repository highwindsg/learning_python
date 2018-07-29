#try to refer to ex35.py
#create functions for different choices
#and within each choice functions, have their own mini story line.
from sys import exit

def slytherin():
    print("You now follow the Slytherin prefects who just stares blankly at you.")
    print("You arrived at a basement that looks like dungeons and sees other fellow Slytherins.")
    exit(0)

def gryffindor():
    print("You now follow the Gryffindor prefects who are very friendly and chatty.")
    print("You arrived at the upper levels that looks like a tower and sees other fellow Gryffindors.")
    exit(0)

def rohan():
    print("You were lead into the golden great hall of the Rohirrim.")
    print("And your trainer presented you with a new training swoord.")
    exit(0)

def minastirith():
    print("You were brought to the steward of the castle of Minas Thrith.")
    print("The steward assigns you to be trained by his own son, Boromir.")
    exit(0)

print("\n")
print("You are born to this world and are now presented with two choices.")
print("Would you choose the Book or the Sword?")
print("1. Book")
print("2. Sword")
print("[Press 1 or 2 and press Enter]")

choice = input("> ")

if choice == "1":
    print("Which type of characteristics below best describes you?")
    print("Choose wisely:")
    print("1. Dark and Quiet")
    print("2. Brave and Strong")
    print("[Press 1 or 2 and press Enter]")

    classes = input("> ")

    if classes == "1":
        slytherin()
    elif classes == "2":
        gryffindor()
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
        rohan()
    elif swordsmen == "2":
        minastirith()
    else:
        print("Well ... not choosing {swordsmen} any I see. Perhaps you wish to reconsider.")


else:
    print("Perhaps you wish you were never born, I think.")

