the_alphabets = ["A", "B", "C", "D", "E"]
the_durians = ["MSW", "D24", "XO", "Bamboo"]
num = [100, 200, 300, 400, 500]

for number in num:
    print(f"This is {number}")

for durian in the_durians:
    print(f"This variety of {durian} is delicious.")

for ABCs in the_alphabets:
    print(f"Today I've learned the alphabet {ABCs}.")

for i in num:
    print(f"I got {i} points!")

for i in the_durians:
    print(f"I get to eat {i} today!")

for _ in num:
    print(f"I get {_} points for today's assessment.")

#creating a new empty list.
new_elements = []

#using range function to do 0 to 6 but not include 6.
for i in range(0, 6):
    print(f"Adding {i} to the new list of elements.")
#dot append is a option that list function understands to concatenate behind.
    new_elements.append(i)

#then now we print out the new filled in list.
for i in new_elements:
    print(f"New element now is: {i}")

