#!/usr/bin/env python3

# https://www.youtube.com/watch?v=daefaLgNkw0

student = {
	"name": "John",
	"age": 25,
	"courses": ["Math", "CompSci"]
}

print(student)
# Using the .get() method and pass in the key as param will prevent a python error from stopping the program.
# This is a good practice to use the .get() method.
print(student.get("name", "Not found"))     # If the first key param of "name" is not in the dict, then the second
# param of "Not found" will be printed instead of None.
print(student.get("courses", "Not found"))
print(student.get("country", "Not found"))
print(student.get("state", "Not found"))
print(student.get("age", "Not found"))
print("")

# Adding a key of "phone" with value.
student["phone"] = "555-5555"
# Change a value of an existing key.
student["name"] = "Jane"
print(student)
print("")

# To update changes of more than one value in the dict, use the .update() func method.
student.update({
	"name": "Jason",
	"age": 36,
	"phone": "555-6666"
})
print(student)
print("")

# To delete a key and it's value, use the del python keyword cmd.
del student["age"]      # To delete the key and value of "age".
print(student)

# Can also use the .pop() func method to delete or remove the last item in the dict. And then assign it to the var
# phone and print out the value of phone.
phone = student.pop("phone")
print(phone)
print(student)
print("")

# To print out how many keys are in the dict.
print(len(student))
# To print out all the keys only from the dict.
print(student.keys())
# To print out all the values only from the dict.
print(student.values())
# To print out all the keys and values pair items from the dict.
print(student.items())
print("")

# To print out all the items using a loop through method.
for key, value in student.items():      # Therefore for every key and value in the student dict, get the .items()
	# func method.
	print(key, value)       # And then print out the key and value.
