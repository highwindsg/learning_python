stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

def displayInventory(self):     # Define a function named 'displayInventory' with
                                # it's own self parm.
    print("Inventory:")
    item_total = 0              # First start the item_total with 0.
    for k, v in self.items():   # For whatever are the items in self, assign it
                                # with k(key) and v(value).
        print(str(v) + ' ' + k)     # Print the string v first, then k.
        item_total = item_total + v # Same as incremental of x = x + 1
    print("Total number of items: " + str(item_total))

displayInventory(stuff)         # Finally pass the 'stuff' var which is the dict
                                # into the displayInventory() function.

# More important to understand line 3 to line 11 of how the for loop is prepared.
# Then line 13 is just to pass in whatever dict var that is declared in line 1,
# which is eg. stuff.
