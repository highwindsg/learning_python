def spam():
    eggs = "spam local"
    print(eggs)     # prints "spam local"

def bacon():
    eggs = "bacon local"
    print(eggs)     # prints "bacon local"
    spam()
    print(eggs)     # prints "bacon local"

eggs = "global"

bacon()
print(eggs)     # prints "global"

# (line 2) A variable named eggs that exists in a local scope when spam() is called.
# (line 6) A variable named eggs that exists in a local scope when bacon() is called.
# (line 11) A variable named eggs that exists in the global scope.”

# “Since these three separate variables all have the same name, it can be confusing to keep track of which one is being used at any given time. This is why you should avoid using the same variable name in different scopes.”
