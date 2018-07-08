print("""You are born to this world
and are now presented with two choices.
Would you choose the Book or the Sword?""")

choice = input("> ")

if choice == "Book":
    print("There are the two different classes of discipline.")
    print("Pick one discipline.")
    print("1. Warlock")
    print("2. Cleric")

    classes = input("> ")

    if classes == "1":
        print("House of Slithrins you go!")
    elif classes == "2":
        print("House of Griffindor you go!")
    else:
        print(f"Well ... not choosing {classes} any I see. Perhaps you wish to reconsider")

elif choice == "Sword":
    print("There are two types of swordmen discipline to train in.")
    print("Pick one type of training.")
    print("1. Ranger")
    print("2. Knight")

    swordsmen = input("> ")

    if swordsmen == "1":
        print("The camp of Rohan you go!")
    elif swordsmen == "2":
        print("The camp of White Castle you go!")
    else:
        print("Well ... not choosing {swordsmen} any I see. Perhaps you wish to reconsider")

else:
    print("Perhaps you wish you were never born, I think")

