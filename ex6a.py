types_of_trees = 5
x = f"There are {types_of_trees} types of trees in the forest."

leaves_color = "red"
bark_type = "rough"
y = f"The trees with {leaves_color} colored leaves and {bark_type} bark surface are known as maple trees."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

animal = "squirrel"
tree_top = "Hey what's that on the tree top? It is a {}"
print(tree_top.format(animal))

left = "On the west side of the forest there's a lake."
right = " And on the east side are many houses."
print(left + right)
