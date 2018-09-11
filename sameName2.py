def spam():
    global eggs     # 'global' here is a Python keyword.
    eggs = "spam"

eggs = "global"
spam()
print(eggs)

# “Because eggs is declared global at the top of spam() (line 2), when eggs is set to 'spam' (line 3), this assignment is done to the globally scoped spam. No local spam variable is created.”
# Therefore when you run this program, the final print() call will output only 'spam'.
