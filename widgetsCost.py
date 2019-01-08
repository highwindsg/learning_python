#!/usr/bin/env python3

COST_PER_WIDGET = 7.49  # Constant price of one widget
nWidgets = int(input("How many widgets do you want to buy? "))
if nWidgets == 1:
    print("One widget will cost you $", COST_PER_WIDGET)
else:
    cost = nWidgets * COST_PER_WIDGET
    print(nWidgets, "widgets will cost you $", cost)

