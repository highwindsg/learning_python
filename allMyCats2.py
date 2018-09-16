catNames = []   # Create a empty list to variable catNames.
while True:
    print("Enter the name of cat " + str(len(catNames) + 1) + " (Or enter nothing to stop.):")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]    # List concatenation.
print("The cat names are:")
for name in catNames:
    print("  " + name)

# len(catNames) is to calculate the length or number of catNames that is added to the catNames list.
