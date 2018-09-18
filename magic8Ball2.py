import random

messages = ["It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Conentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful"]

# Therefore print a random line of message from the list above.
# len(messages) shows there are 9 lines.
# A random line number will be obtained between 'len(messages) - 1' and the
# benefit of this approach is that you can add and remove strings to the
# messages list without changing other lines of code.
print(messages[random.randint(0, len(messages) - 1)])
