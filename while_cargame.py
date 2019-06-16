#!/usr/bin/env python3

command = ""

started = False

while True:
    command = input("> ").lower()   # '.lower()' is set here to accept any case
                                    # sensitive entries.
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that!")

