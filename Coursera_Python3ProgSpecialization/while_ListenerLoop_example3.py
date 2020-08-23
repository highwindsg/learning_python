#!/usr/bin/env python3

"""
In a grocery store, there’s a little plastic bar that you put
after your last item to separate your groceries from those of
the person behind you; that’s how the cashier knows you have no
more items. We don’t have a “little plastic bar” data type in
Python, so we’ll do the next best thing: we will use a price of
zero to mean “this is my last item.”
"""

def checkout():
    total = 0   # Accumulator var to show the total sum at a certain point.
    count = 0   # Accumulator var counter to count the number of items.

    moreItems = True
    while moreItems:    # This means True so that while loop can continue.
        price = float(input("Enter price of item (0 when done): "))
        
        if price < 0:
            print("Invalid entry, try again.") 
        elif price != 0:
            total = total + price
            count += 1
            print("Subtotal: $", total)
            print("")
        else:
            moreItems = False   # If False then exit the while loop.

            
    average = total / count
    print("Total items:", count)
    print("Total $", total)
    print("Average price per item: $", average)

checkout()

print("")
