#!/urs/bin/env python3

# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)

# Display lengths
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))
print("")

# Iterate over both sequences
for p in prime_numbers:
    print("Prime: ", p)
for n in perfect_squares:
    print("Square: ", n)
print("")

# To display the methods available to list and tuple.
# You will see that list have more methods than compared to tuple.
# Therefore list occupy more memory than tuple.
print("List methods")
print(dir(prime_numbers))
print(80 * "-")
print("Tuple methods")
print(dir(perfect_squares))
print(80 * "-")
print("")

# To compare the memory size between list and tuple.
import sys  # The sys module means system. Contains a wealth of system specific functionality.

print("sys module available methods")
print(dir(sys))  # To see available methods provided by the sys module.
print(help(sys.getsizeof))  # The sys.getsize() method will show the size of an object in bytes.
print("")

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

# The output will show that list occupy more memory bytes than tuple.
print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

# Tuples can also be made more quickly than lists.
# We use a timeit module to see how long it takes for the computer to make one million lists and one million of tuples.
import timeit

# From timeit mobule, use the timeit method and pass in the params of a list statement and a number of one million.
# The output will show how long it takes to make a million of this list.
list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

# The output will show that it takes more time to make a list than compared to making a tuple.
# Imagine if dealing with billions of data and the amount of time it will take and considering bandwidth transmit time.
print("List time: ", list_test)
print("Tuple time: ", tuple_test)
print("")

# To make an empty tuple.
empty_tuple = ()
test1 = ("a",)  # To print a single string tuple, must put a comma before close bracket,
# else will be treated as a string.
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)
print("")

# For integer values, you can create tuples straight away.
test_1 = 1,  # To print a single int tuple, must put a comma after the single int.
test_2 = 1, 2
test_3 = 1, 2, 3
print(test_1)
print(test_2)
print(test_3)
print(type(test_1))
print(type(test_2))
print(type(test_3))
print("")

# (age, country, knows_python)
survey = (27, "Vietnam", True)

# Assigning tuple components to individual var.
age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print("")

# Tuple unpacking and assigning values in order, in a single line.
# Make sure that the number of vars matches the number of elements in the tuple.
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print("")
