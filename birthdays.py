birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":      # Without line 6 and 7, the program will not break to exit
        break           # if a blank in entered.

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("When is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")

# Line 1: You create an initial dictionary and store it in birthdays.
# Line 9: You can see if the entered name exists as a key in the dictionary with the 'in' keyword.
# LIne 10: Just as you did for lists, if the name is in the dictionary, you access the associated value
# using square brackets in line 10.
# If not, you can add it using the same square bracket syntax (line 15)
# combined with the assignment operator '='.
