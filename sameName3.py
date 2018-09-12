def spam():
    global eggs
    eggs = "spam"   # This is the global.

def bacon():
    eggs = "bacon"  # This is a local.

def ham():
    print(eggs)     # This is the global.

eggs = 42           # Th is the global

spam()
print(eggs)

# In the spam() function, eggs is the global eggs variable, because there’s a global statement for eggs at the beginning of the function (line 2). In bacon(), eggs is a local variable, because there’s an assignment statement for it in that function (line 6). In ham() (line 8), eggs is the global variable, because there is no assignment statement or global statement for it in that function. If you run sameName3.py, the output will be ”spam".
