#!/usr/bin/env python3

class User:  # Create a class named 'User'.
    pass  # Assign a 'pass' statement to make it an empty class for now.


user1 = User()  # Set var 'user1' to an instance of class 'User()'.
user1.first_name = "Dave"  # Assign an obj attrib of 'first_name' to var 'user1'.
user1.last_name = "Bowman"  # Assign an obj attrib of 'last_name' to var 'user1'.

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

print(user1.first_name)
print(user1.last_name)
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)

"""
There are no limit to the number of objects you can create in a class.
"""
