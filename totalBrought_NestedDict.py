allGuests = {"Alice": {"apples": 5, "pretzels": 12},
             "Bob": {"ham sandwiches": 3, "apples": 2},
             "Carol": {"cups": 3, "apple pies": 1}}

# Inside the 'totalBrought()' function, the for loop iterates over the
# key-value pairs in guests.
def totalBrought(guests, things):
    numBrought = 0
    for k, v in guests.items():     # The string of the guest's name is assigned to k,
                                    # and the dict of the items they're are bringing are
                                    # assigned to v.
        numBrought = numBrought + v.get(things, 0)  # If the things parm exists as a key
                                                    # in this dict, it's value (the qty)
                                                    # is added to numBrought.
                                                    # If it does not exists as a key, the
                                                    # get() method returns 0 to be added
                                                    # to numBrought.
    return numBrought

print("Number of things being brought:")
print(" - Apples            " + str(totalBrought(allGuests, "apples")))
print(" - Cups              " + str(totalBrought(allGuests, "cups")))
print(" - Cakes             " + str(totalBrought(allGuests, "cakes")))
print(" - Ham Sandwiches    " + str(totalBrought(allGuests, "ham sandwiches")))
print(" - Apple Pies        " + str(totalBrought(allGuests, "apple pies")))

