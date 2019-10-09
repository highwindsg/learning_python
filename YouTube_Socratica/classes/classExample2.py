#!/usr/bin/env python3

import datetime  # Import the datetime library for displaying date.


class User:  # Create a class named 'User'.
    def __init__(self, full_name, birthday):  # Define a init start func with params 'self', 'full_name' and 'birthday'.
        self.name = full_name  # From self, set the obj 'name' with the value from param 'full_name'.
        self.birthday = birthday  # yyyymmdd  # From self, set the obj 'birthday' with the value from param 'birthday'.

        """ Extract first name and last name by splitting the full name using the .split() method,
        and assign to var 'name_pieces'. Also, there are no limits to the number of self.objects you can
        create in a class. """
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]  # Index 0 is the first name.
        self.last_name = name_pieces[-1]  # Index -1 counts backwards and that will be the last name.

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)  # We purposely set the year datt month to standardize the answer.
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)  # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("Dave Middle Bowman", "19710315")  # Set 'User' class with two params values of actual name and birthday,
# and assign to var 'user'.
print(user.name)  # Print out the values of 'name' of var 'user' which is from -> 'self.name' obj.
print(user.birthday)  # Print out the values of 'birthday' of var 'user' which is from -> 'self.birthday' obj.
print(user.first_name)  # Print out the values of 'first_name' of var 'user' which is from -> 'self.first_name' obj.
print(user.last_name)  # Print out the values of 'last_name' of var 'user' which is from -> 'self.last_name' obj.
print(user.age())
help(User)  # This is a 'help()' function for the 'User' class.
