print("Below is example of a list.")
things = ['a', 'b', 'c', 'd']
print(things)

print("Below prints out the first index of the list.")
print(things[1])

print("Below changes the first index item in the list to 'z'.")
things[1] = 'z'
print(things[1])

print(things)
print("\n")

print("Below is an example of a dictionary named 'stuff'.")
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff)

print("Below prints out the key of value name from the stuff dictionary.")
print(stuff['name'])

print("Below prints out the key of value age from the stuff dictionary.")
print(stuff['age'])

print("Below prints out the key of value height from the stuff dictionary.")
print(stuff['height'])

print("And below here we append in the new key of city with value of SF into the dictionary.")
stuff['city'] = "SF"

print("And so we print out the value from the key of city from the dictionary.")
print(stuff['city'])
print("\n")

print("Below is example of appending new keys and values into the dictionary with strings.")
print("Newly appended keys are named as 1 and 2 with their respective values.")
stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff)

print("And we print out only the two newly added values.")
print(stuff[1])
print(stuff[2])
print("\n")

print("Below example shows how to delete things in the stuff dictionary.")
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

