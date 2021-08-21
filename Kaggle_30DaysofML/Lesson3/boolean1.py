#!/usr/bin/env python3

# Create func that returns the boolean value.
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35


print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))
print("")



# Create func that check if a number is odd by checking that the
# modulud with 2 returns 1.
def is_odd(n):
    return (n % 2) == 1

"""Remember to use == instead of = when making comparisons. 
If you write n == 2 you are asking about the value of n. 
When you write n = 2 you are changing the value of n."""

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))
print("")



# Create a func that returns the boolean value by changing the earlier
# can_run_for_president() function.
def can_run_for_president2(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run
    for president in the US?"""
    # The US Constitution says you must be a natural born citizen
    # and also at least 35 years old.
    return is_natural_born_citizen and (age >= 35)


print(can_run_for_president2(19, True))
print(can_run_for_president2(55, False))
print(can_run_for_president2(55, True))
print("")



"""What is the value of the below expression?"""
print(True or True and False)
"""NOTE: For boolean, the order of operation will first 
evaluate 'and' before 'or'."""
print("")



"""
Python has a bool() function which turns things into bools.
"""
print(bool(1)) # all numbers are treated as true, except 0.
print(bool(0))
print(bool("asdf")) # all things are treated as true, except the empty string "".
print(bool(""))
print("")
