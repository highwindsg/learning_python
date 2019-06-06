#!/usr//bin/env python3

birth_year = input("Birth year: ")  # Ask user to enter year of birth.
print(type(birth_year))             # Print out the data type of var birth_year.
age = 2019 - int(birth_year)        # Assume current year is 2019, less off the
                                    # var birth_year in integer data type.
print(type(age))                    # Print out the data type of age.

# Finally print out the statement to tell the user how old is he/she by putting
# the data type of age in str, else age cannot be printed out.
print("Your are " + str(age) + " years old")

