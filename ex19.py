def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You now have {cheese_count} cheeses!")
	print(f"And also you have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print("Still we can ask how many cheese and crackers you want.")
num_cheese = input("How may cheese do you want?: ")
num_boxes = input("How many boxes of crackers do you want?: ")
cheese_and_crackers(num_cheese, num_boxes)
