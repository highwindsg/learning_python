#!/usr/bin/env python3

'''
1. The new class (child) has all the capabilities of the old class (parent) - and then with some more things.
2. The new (child) class reuse an existing class and 'inherit' all the capabilities of an existing class.
3. Therefore, we write once, reuse many times.
4. 'Subclasses' is another way of describing a child class, which 'inherit' attributes and behaviours from
their parent classes, and can introduce their own.
'''


class PartyAnimal:  # Create a class named 'PartyAnimal'.
    x = 0   # Set var 'x' to 0 first.
    name = ""  # Set var 'name' to nothing first.

    def __init__(self, nam):  # Create a init start (constructor) func with params self and nam.
        self.name = nam  # From self, set the .name var to param 'nam'.
        print(self.name, "constructed")  # Print out the value of 'self.name'.

    def party(self):  # Create a party func with param self.
        self.x = self.x + 1  # Add self.x by 1 count, and assign it back to var self.x
        print(self.name, "party count", self.x)


class FootballFan(PartyAnimal):  # Create a child class named 'FootballFan' that has a param that inherits
    # from parent class 'PartyAnimal'. This way class 'FootballFan' can use all the var objs that are from
    # the parent class.
    points = 0  # Set var 'points' to 0 first.

    def touchdown(self):  # Create a touchdown func with param 'self'.
        # Note that this child class got no 'init' start func, so it will automatically inherit the 'init' start func
        # and suit from the parent class.
        self.points = self.points + 7  # Add self.points by 7 count, and assign it back to var self.points.
        self.party()  # From self, call the 'party' func.
        print(self.name, "points", self.points)  # Print out the value of 'self.name and 'self.points'.


s = PartyAnimal("Sally")  # Var 's' is-a 'PartyAnimal' class with param 'Sally'.
s.party()  # Client call var 's' with the attrib of party() func.

j = FootballFan("Jim")  # Var 'j' is-a 'FootballFan' class with param 'Jim'.
j.party()  # Client call var 'j' with the attrib of party() func.
j.touchdown()  # Client call var 'j' with the attrib of touchdown() func.
