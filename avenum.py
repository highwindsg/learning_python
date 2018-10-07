total = 0
count = 0

while (True):
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
