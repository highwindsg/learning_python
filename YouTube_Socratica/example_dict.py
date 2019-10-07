#!/usr/bin/env python3

post = {"user_id": 209,
        "message": "D5 E5 C5 C4 G4",
        "language": "English",
        "datetime": "20230215T123231Z",
        "location": (44.590533, -104.715556)
        }

print(post)
print(type(post))
print("")

# Creating a dict using a dict constructor.
post2 = dict(message="SS Cotopaxi", language="English")
print(post2)

# Adding new keys and values into the existing dict of post2.
# Note that when entering new keys, must use open and close quotes for the keys.
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
print(post2)
print(type(post2))
print("")

# Accessing data from a dictionary.
print(post["message"])
print("")

# Example to print out the 'location' key value, though it does not exist in dict post2.
if "location" in post2:
    print(post2["location"])
else:
    print("The post does not contain a location value.")
print("")

# Can use the 'try and except' method to handle error message.
try:
    print(post2["location"])
except KeyError:
    print("The post does not have a location.")
print("")

""" It is possible to access data from a dictionary in situation whereby it is possible
the value does not have a key to match. """
# Display the directory for the post2 dict.
print(dir(post2))   # Use dir(post2) to see what methods available.
help(post2.get)     # Use the help method to see what how to use the .get method on dict post2.

print(post)

for key in post.keys():
    value = post[key]
    print(key, "=", value)
print("")

# Alternatively, another way to iterate key and value in a dict.
for key, value in post.items():
    print(key, "=", value)
print("")

print(dir(post))
help(post.pop)
help(post.popitem())


