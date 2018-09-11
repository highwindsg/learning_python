while True:
    print("Who are you?")
    name = input()
    if name != "Caven":
        continue
    print("Hello, Caven. What is the password? (It is a type of fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access granted.")
