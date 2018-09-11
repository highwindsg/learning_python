import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"

r = random.randint(1, 9)    # Random integers are evaluated between 1 and 9, (including 1 and 9).
fortune = getAnswer(r)
print(fortune)

# The single line below is equivalent to combining the 3 lines (22, 23, 24) above.
print(getAnswer(random.randint(1, 9)))
