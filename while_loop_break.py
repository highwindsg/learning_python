#!/usr/bin/env python3

questions = [                   # First prepare the questions in a list.
"What is your name?",
"What is your favorite color?",
"What is your quest?"
]

n = 0                           # Let the index variable of the questions
                                # starts at 0 and assign to variable 'n'.

while True:
    print("Type q to quit")
    a = input(questions[n])     # Ask for inputs to the questions list and
                                # assigns the answers back to variable 'a'.
    if a == "q":                # Sets a condition if the input is 'q',
        break                   # then the loop with stop or break.
    n = (n + 1) % 3
"""Each time around the loop, you assign 'n' to the evaluation of the
expression (n + 1) % 3, which enables you to cycle indefinitely through
every questions in your 'questions' list.

The first time around the loop, 'n' starts at '0'.
Next, 'n' is assigned the value of the expression (0 + 1) % 3,
which evaluates to 1.

Then, 'n' is assigned to the value of (1 + 1) % 3,
which evaluates to 2, because whenever the first number in an expression
using modulo is smaller than the second, the answer is the first number.

Finally, 'n' is assigned the value of (2 + 1) % 3, which evaluates
back to 0.
"""
