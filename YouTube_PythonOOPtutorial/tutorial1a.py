#!/usr/bin/env python3


class Player:   # Create a class named Player.

	num_of_p = 0    # Set a class var of num_of_p to start with a value of 0.

	# Define a init constructor with params self, char_class, hit_point, magic_point and weapon.
	def __init__(self, gender, char_class, hit_point, magic_point, weapon):
		self.gender = gender    # From self, set a instance var of gender and assign it to gender.
		self.char_class = char_class    # From self, set a instance var of char_class and assign it to char_class.
		self.hit_point = hit_point  # From self, set a instance var of hit_point and assign it to hit_point.
		self.magic_point = magic_point  # From self, set a instance var of magic_point and assign it to magic_point.
		self.weapon = weapon    # From self, set a instance var of weapon and assign it to weapon.
		self.constitution = hit_point + magic_point     # From self, add a new instance var of constitution and assign
		# it to the sum of hit_point and magic_point.

		Player.num_of_p += 1    # From the Player class, instantiate a class var of num_of_p to increase by 1.


# set Player class to an instance of var p1 with params.
p1 = Player("male", "warrior", 80, 20, "sword")
p2 = Player("female", "cleric", 60, 50, "staff")

print("The character is a", p1.gender + " " + p1.char_class + ".")
print("He has", str(p1.hit_point) + " hit point and " + str(p1.magic_point) + " magic point.")
print("The", p1.char_class + " also wields a " + p1.weapon + ".")
print("This", p1.char_class + " has a total constitution of " + str(p1.constitution) + ".")
print("")

print("The number of players are", + Player.num_of_p, ".")  # This will print out the total number of players as var
# p1 and p2 are created, instantiated in line 22 and 23.

