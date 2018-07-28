print("\n")
print("How many people are attending?", end=' ')
people = int(input())

print("How many slices of cakes did we bought?", end=' ')
cake_slices = int(input())

print("How many slices of pizzas did we bought?", end= ' ')
pizza_slices = int(input())

print("How many cans of drinks did we bought?", end=' ')
drinks = int(input())

print("\n")
if people > cake_slices:
    print("We do not have enough cakes to go around.")
elif people < cake_slices:
    print("We have enough cakes for everyone.")
else:
    print("We are not sure if there are enough cakes.")

if people > pizza_slices:
    print("We do not have enough pizzas to go around.")
elif people < pizza_slices:
    print("We have enough pizza slices to go around.")
else:
    print("We are not sure if pizzas are enough for everyone.")

if people > drinks:
    print("We do not have enough drinks to go around.")
elif people < drinks:
    print("We have enough drinks for everyone.")
else:
    print("We are not sure if there are enough drinks for everyone.")
print("\n")
