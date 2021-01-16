#!/usr/bin/env python3
"""
The split method breaks a string into a list of words.
"""

song = "The rain in Spain..."
wds = song.split()
print(wds)
print("")


"""
An optional argument called a delimiter can be used to specify which
characters to omit in the list.
"""

wds2 = song.split("ai")
print(wds2)
print("")


"""
Create a new list of the 6th through 13th elements of lst (eight items in all)
and assign it to the variable output.
"""

lst = [
    "swimming",
    2,
    "water bottle",
    44,
    "lollipop",
    "shine", 
    "marsh", 
    "winter", 
    "donkey", 
    "rain", 
    ["Rio", "Beijing", "London"], 
    [1,2,3], 
    "gold", 
    "bronze", 
    "silver", 
    "mathematician", 
    "scientist", 
    "actor", 
    "actress", 
    "win", 
    "cell phone", 
    "leg", 
    "running", 
    "horse", 
    "socket", 
    "plug", 
    ["Phelps", "le Clos", "Lochte"], 
    "drink", 
    22, 
    "happyfeet", 
    "penguins"
    ]

output = lst[5:13]
print(output)
print("")


"""
Create a variable output and assign it to a list whose elements are the words 
in the string str1.
"""

str1 = "OH THE PLACES YOU'LL GO"
output = str1.split()
print(output)
print("")


"""
Write a program that will print out the length of each item in the list as 
well as the first and last characters of the item.
"""

weather = [
    "sunny",
    "cloudy",
    "partially sunny",
    "rainy",
    "storming",
    "windy",
    "foggy",
    "snowy",
    "hailing"
    ]

for condition in weather:
    print("The word is", len(condition), "characters")
    first_char = condition[0]
    last_char = condition[-1]
    print("The first character is: " + first_char)
    print("The last character is: " + last_char)

print("")


"""
Write code to determine how many t's are in the following sentences.
"""

phrases = [
    "My, what a lovely day today is!",
    "Have you mastered cooking yet? A tasty treat could be in your future.",
    "Have you ever seens the leaves change color?"
    ]

for sentence in phrases:
    print(sentence.count("t"))  # using the .count() method with letter 't' as argument.

print("")


"""
Write a program that extracts the last three items in the list sports and assigns 
it to the variable last. Make sure to write your code so that it works no matter 
how many items are in the list.
"""

sports = [
    'cricket', 
    'football', 
    'volleyball', 
    'baseball', 
    'softball', 
    'track and field', 
    'curling', 
    'ping pong', 
    'hockey'
    ]

last = (sports[-3:])
print(last)
print("")


"""
What will the output be for the following code?
"""

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)
print("")


"""
Write code to determine how many 9’s are in the list nums and assign that value to the 
variable how_many. Do not use a for loop to do this.
"""

nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

how_many = (nums.count(9))
print(how_many)
print("")


"""
Write code that uses slicing to get rid of the second 8 so that there are only two 8’s in the list 
bound to the variable nums.
"""

nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

#print(nums[4])
#nums.pop(4)
del nums[4:5]
print(nums)
print("")


"""
Assign the number of elements in lst to the variable num_lst.
"""

lst = [
    "hi", 
    "goodbye", 
    "python", 
    "106", 
    "506", 
    91, 
    ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 
    109, 
    "chair", 
    "pizza", 
    "wolverine", 
    2017, 
    3.92, 
    1817, 
    "account", 
    "readings", 
    "papers", 
    12, 
    "facebook", 
    "twitter", 
    193.2, 
    "snapchat", 
    "leaders and the best", 
    "social", 
    "1986", 
    9, 
    29, 
    "holiday", 
    ["women", "olympics", "gold", "rio", 21, "2016", "men"], 
    "26trombones"
    ]

num_lst = len(lst)
print(num_lst)
print("")


"""
Create a variable called wrds and assign to it a list whose elements are the words in the string sent. 
Do not worry about punctuation.
"""

sent = "The bicentennial for our university was in 2017"

wrds = sent.split()
print(wrds)
print("")
