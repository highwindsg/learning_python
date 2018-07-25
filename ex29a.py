cakes = input("How many pieces of cakes do we have?: ") 
cookies = input("How many cookies do we have?: ")
people = input("How many people are coming?: ")
print("\n")

if people < cakes:
    print("There's enough cakes for everyone!")

if people > cakes:
    print("There are not enough cakes for everyone!")

if cookies > people:
    print("There's enough cookies for everyone!")

if cookies < people:
    print("There are not enough cookies for everyone!")

if cakes == cookies:
    print("We have the same amount of food.")

if cakes != cookies:
    print("We do not have the same amount of food.")

if people >= cookies + cakes:
    print("We do not have enough food for everyone!")

if people <= cookies + cakes:
    print("We have enough food for everyone!")

print("\n")
