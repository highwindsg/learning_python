x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

if x == y:
    print("x and y are equal")
else:
    if x < y:
        print("x is less than y")
    else:
        print("x is greater than y")

# Line 7 to 10 is a nested conditional.
# Unless necessary, it is better to avoid them as they quickly become difficult to read.
