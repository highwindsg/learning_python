#!/usr/bin/env python3

grocery_item = ""
grocery_list = []

while grocery_item != "done":
    grocery_item = input("Please write down an item to add to your list and when finished, type 'done'. ")
    if grocery_item == "done":
        continue
    else:
        print("Adding item to the list.")
        grocery_list.append(grocery_item)

print("Here is our grocery list:")
print(grocery_list)

