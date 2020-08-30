#!/usr/bin/env python3

"""
Q1.
Create a function called mult that has two parameters, the first
is required and should be an integer, the second is an optional
parameter that can either be a number or a string but whose
default is 6. The function should return the first parameter
multiplied by the second.
"""

def mult(int, str = 6):
    return int * str


print("Q1 answer:")
print(mult(5, 6))
print(mult("Hello"))
print("")


"""
Q2.
The following function, greeting, does not work. Please fix the
code so that it runs without error. This only requires one change
in the definition of the function.
"""

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl


print("Q2 answer:")
print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))
print("")


"""
Q3.
Below is a function, sum, that does not work. Change the function
definition so the code works. The function should still have a
required parameter, intx, and an optional parameter, intz with a
defualt value of 5.
"""

def sum(intx, intz=5):
    return intz + intx


print("Q3 answer:")
print(sum(3))
print(sum(3, 10))
print("")


"""
Q4.
Write a function, test, that takes in three parameters: a required
integer, an optional boolean whose default value is True, and an
optional dictionary, called dict1, whose default value is
{2:3, 4:5, 6:8}. If the boolean parameter is True, the function
should test to see if the integer is a key in the dictionary.
The value of that key should then be returned. If the boolean
parameter is False, return the boolean value “False”.
"""

def test(int, bol = True, dict1 = {2:3, 4:5, 6:8}):
    return bol and dict1.get(int, False)


print("Q4 answer:")
print(test(2, True))
print(test(7, True))
print(test(5, dict1 = {5:4, 2:1}))
print("")


"""
Q5.
Write a function called 'checkingIfIn' that takes three parameters.
The first is a required parameter, which should be a string.
The second is an optional parameter called direction with a
default value of True. The third is an optional parameter called
'd' that has a default value of
{
    'apple': 2, 
    'pear': 1, 
    'fruit': 19, 
    'orange': 5, 
    'banana': 3, 
    'grapes': 2, 
    'watermelon': 7
    }.
Write the function checkingIfIn so that when the second parameter
is True, it checks to see if the first parameter is a key in the
third parameter; if it is, return True, otherwise return False.

But if the second paramter is False, then the function should
check to see if the first parameter is not a key of the third.
If it’s not, the function should return True in this case, and if
it is, it should return False.
"""

def checkingIfIn(str, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if str in d:
            return True 
        else:
            return False
    else:
        if str not in d:
            return True
        else:
            return False


print("Q5 answer:")
print(checkingIfIn("grapes"))
print(checkingIfIn("pear"))
print(checkingIfIn("durian"))
print("")


"""
Q6.
We have provided the function checkingIfIn such that if the first
input parameter is in the third, dictionary, input parameter,
then the function returns that value, and otherwise, it returns
False. Follow the instructions in the active code window for
specific variable assignmemts.
"""

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]


# Call the function so that it returns False and assign that function call to the
# variable c_false
print("Q6 answer:")
c_false = (checkingIfIn("durian"))
print(c_false)

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
print(c_true)

# Call the function so that the value of fruit is assigned to the variable
# fruit_ans
fruit_ans = checkingIfIn('fruit')
print(fruit_ans)

# Call the function using the first and third parameter so that the value 8 is
# assigned to the variable param_check
param_check = checkingIfIn('potatos', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
print(param_check)

print("")
