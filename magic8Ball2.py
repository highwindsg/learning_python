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
# random.randint() will choose a random line number.
print(messages[random.randint(0, len(messages) - 1)])
