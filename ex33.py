i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers)

    i = i + 1
    print(f"At the bottom i is {i}")
    print("\n")

print("The numbers: ")

for num in numbers:
    print(num)

