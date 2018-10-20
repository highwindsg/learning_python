#!/usr/bin/env python3
# Chatbot - random-only version
# Example program from Raspberry Pi For Dummies

import random   # To bring in the 'random' module for generating random nos.

# The list below 'random_replies' contains statements the computer can output
# in response to whatever the user enters. The more responses there are,
# the more effective the illusion of intelligence is.
random_replies = ["Oh really?",
                  "Are you sure about that?",
                  "Hmmmmm.",
                  "Interesting...",
                  "I'm not sure I agree with that...",
                  "Definitely!",
                  "Maybe!",
                  "So what are you saying, exactly?",
                  "Meaning what?",
                  "You're probably right.",
                  "Rubbish! Absolutely nonsense!",
                  "Anyway, what are your plans for tomorrow?",
                  "That seems to be a popular viewpoint.",
                  "A lot of people have been telling me that.",
                  "Wonderful!",
                  "That could be a bit embarassing!",
                  "Do you really think so?",
                  "Indeed...",
                  "My point exactly!",
                  "Perhaps..."]

# Making the chatbot asking the user a question.
print("What's on your mind?")

# To use a var 'user_says' later in the while loop, need to set it up first.
user_says = ""
# Using a while loop to keep the conversation going until the user says 'bye'.
# Request input from user using the 'input()' function. And whatever the user
# enters is stored in a var 'user_says'.
while user_says != "bye":
    user_says = input("Talk to me: ")

# The next line picks and index no. for the random response.
# Give 'random.randint()' function two nos. to work with (or two arguments).
# The first no. is the smallest possible no. '1'.
# The second is the highest possible no., which is the length of the no. of
# possible 'random_replies'. And the random int being picked will be stored
# in the var 'reply_chosen'.
# And because list indexes start counting at 0, you need to subtract 1 from
# the random number. (eg. - 1)
    reply_chosen = random.randint(1, len(random_replies)) - 1

# The final two lines print the randomly selected list items and then replace
# that list item with whatever the user entered.
    print(random_replies[reply_chosen])
    random_replies[reply_chosen] = user_says

