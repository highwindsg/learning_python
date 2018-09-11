import sys

while True:
    print("Type exit to exit.")
    response = input()      # Assign the variable response with the input() of what you typed in.
    if response == "exit":
        sys.exit()          # From the module sys, get the exit function.
    print("You typed " + response + ".")    # Insert what you typed in, into the print statement
                                            # between the two plus signs.
