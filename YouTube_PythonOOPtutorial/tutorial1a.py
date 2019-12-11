#!/usr/bin/env python3


class Player:   # Create a class named Player.

	# Define a init constructor with params self, char_class, hit_point, magic_point and weapon.
	def __init__(self, gender, char_class, hit_point, magic_point, weapon):
		self.gender = gender    # From self, set a instance var of gender and assign it to gender.
		self.char_class = char_class    # From self, set a instance var of char_class and assign it to char_class.
		self.hit_point = hit_point  # From self, set a instance var of hit_point and assign it to hit_point.
		self.magic_point = magic_point  # From self, set a instance var of magic_point and assign it to magic_point.
		self.weapon = weapon    # From self, set a instance var of weapon and assign it to weapon.
		self.constitution = hit_point + magic_point     # From self, add a new instance var of constitution and assign
		# it to the sum of hit_point and magic_point.


# set Player class to an instance of var P1 with params.
P1 = Player("male", "warrior", 80, 20, "sword")

print("The character is a", P1.gender + " " + P1.char_class + ".")
print("He has", str(P1.hit_point) + " hit point and " + str(P1.magic_point) + " magic point.")
print("The", P1.char_class + " also wields a " + P1.weapon + ".")
print("This", P1.char_class + " has a total constitution of", + P1.constitution, ".")
print("")
