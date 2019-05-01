numlist = list()    # To create an empty list of numbers.

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    numlist.append(value)   # To allow user to add 'append' to the list of numbers.

average = sum(numlist) / len(numlist)
print("Total:", sum(numlist))
print("Count:", len(numlist))
print("Average:", average)
