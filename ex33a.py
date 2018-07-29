i = 0
numbers = []

while i < 10:
    print(f"Now i is {i}")
    numbers.append(i)
    print("So numbers in the list is now: ", numbers)

    i = i + 1
    print(f"And now the new i is {i}")
    print("\n")

print("And so all the numbers are now: ")

for num in numbers:
    print(num)

