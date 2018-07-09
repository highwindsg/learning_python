i = 0
numbers = []

while i < 6:
    print(f"Now, at the top i is {i}")
    numbers.append(i)
    print("So numbers in the list is now: ", numbers)

    i = i + 1
    print(f"And now, at the bottom i is {i}")
    print("\n")

print("The numbers: ")

for num in numbers:
    print(num)

