while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():     # If input age is numeric then we break out of this
        break               # while loop and move on to the next one.
    print("Please enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():  # If input password is alpha-numeric then we break
        break               # out of this while loop and proceed.
    print("Password can only have letters and numbers.")
