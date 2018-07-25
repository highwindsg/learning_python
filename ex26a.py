print("Where are you today?", end= ' ')
where = input()
print("What are you doing today then?", end=' ')
what = input()
print("And how much time did that took?", end=' ')
time = input()

print(f"So you at {where} today attending to a {what} and it took {time}.")

print("**********")

from sys import argv
script, letter = argv
txt = open(letter)

print("Here's your 'letter' today:\n")
print(txt.read())

print("Unsure of the letter's content, enter the name of the letter to read again.")
letter_again = input("> ")
txt_again = open(letter_again)
print(txt_again.read())

print("**********")

print('Let\'s go through what happened today.')
print('I\'d been told by the aircon servicing men \'bout my two aircon compressors \n and \t room units.')
print('That they\'re too old to be serviced.')

print("**********")

poem_today = """
\tRush downstairs to draw money
thinking to pay the fee after servicing \n
\tNot knowing that servicing men
will tell me that \n
\tyour aircon are
too old to maintain. \n
\tSo I\'ll just charge you
$20 for transport fee.
"""
print("----------")
print(poem_today)
print("----------")
print("\n")
print("**********")


