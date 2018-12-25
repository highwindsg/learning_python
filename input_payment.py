#!/usr/bin/env python3

item_cost = float(input("Enter the price of the item: "))
amount_paid = float(input("Enter the amount you are paying: "))
amount_change = float(amount_paid) - float(item_cost)
print("")
print("The item cost $", item_cost, "and you gave", amount_paid, "dollars. Your change is $", amount_change, "dollars.")
print("")
# Alternate display line by line.
print("The item cost $", item_cost)
print("You paid $", amount_paid)
print("Your change is $", amount_change)
