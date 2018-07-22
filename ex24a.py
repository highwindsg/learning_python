print("Let's try to do everything again.")
print('I\'d need to learn \'bout escapes with \\ back-slash to do that to:')
print('\n as well as adding new lines and \t tabs spaces too.')

song = """
Once upon a time there was 
\ta coconut tree. \n
A lion or two \n\tenjoying the breeze.
\nThen came Sengnila Wutama
\tand named it Singapura.
"""

print("--------------------")
print(song)
print("--------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}\n")

def protein_breakfast(started):
    whey_powder = int(started * 5)
    eggs = int(whey_powder / 1000)
    trays = int(eggs / 10)
    return whey_powder, eggs, trays

calories_required = 5000
protein_bars, hardboiled_eggs, tupperware = protein_breakfast(calories_required)

# this a another way to put things in string without the f format in front.
print("With a required calories of: {}".format(calories_required))
print(f"We will have {protein_bars} protein bars, {hardboiled_eggs} of hard boiled eggs and {tupperware} number of tupperware containers to put all in.\n")

calories_required = calories_required / 10

print("We can also do it another way:")
new_formula = protein_breakfast(calories_required)
#below is an easy and direct way to input the things into a string.
print("We'll than have {} protein bars, {} hardboild eggs, and {} number of tubberware containers to contain all.\n".format(*new_formula))

