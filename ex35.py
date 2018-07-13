from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Oh man..., so little??")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy fellow!")


def bear_room():
    print("There is a fat bear here.")
    print("The bear has a bunch of honey.")
    print("However the bear is in front of another door.")
    print("How are you going to move the bear? ('take honey' or 'taunt bear')")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved away from the door.")
            print("You can go through it now.")
            print("So what do you decide to do next? ('take honey', 'taunt bear' or 'open door')")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def bigrock_room():
    print("And you see a great big rock rolling towards you!")
    print("You screamed out loud and almost don't know what to do.")
    print("Do you run for your life or stay put and continue to scream your head off? ('run' or 'stay')")

    choice = input("> ")

    if "run" in choice:
        start()
    elif "stay" in choice:
        dead("The big rock nearly rolls over you.")
    else:
        bigrock_room()

    
def dead(why):
    print(why, "You survived and left. Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your left and right.")
    print("Which one do you take? (left or right)")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        bigrock_room()
    else:
        dead("You stumble around the room until you starve.")


start()

