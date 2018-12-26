#!/usr/bin/env python3

item_cost = float(input("Enter the price of the item: "))
amount_paid = float(input("Enter the amount you are paying: "))
amount_change = float(amount_paid) - float(item_cost)
print("")
print("The item cost $" + str(item_cost) + " and you gave me $" + str(amount_paid) + ". Your change is $" + str(amount_change) + ".")
print("")
# Alternate display line by line.
print("The item cost $" + str(item_cost))
print("You paid $" + str(amount_paid))
print("Your change is $" + str(amount_change))
