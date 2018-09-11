def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

# “Since there is no parameter named eggs or any code that assigns eggs (line 2) a value in the spam() function, when eggs is used in spam(), Python considers it a reference to the global variable eggs (line 3). This is why 42 is printed twice when the previous program is run.”
