inp = input("Enter Fahrenheit Temperature: ")
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 /9.0
    print(cel)
except:
    print("Please enter a number")

# Python starts by executing the sequence of statements in the try block. (line 2 to 5)
# If all goes well, it skips the except block and proceeds.
# If an exception occurs in the try block, Python jumps out of the try block
# and executes the sequence of statements in the except block. (line 6 to 7)

