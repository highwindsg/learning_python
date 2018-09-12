def spam():
    print(eggs)     # ERROR!
    eggs = "spam local"

eggs = "global"
spam()

# This error happens because Python sees that there is an assignment statement for eggs in the spam() function (line 3) and therefore considers eggs to be local. But because print(eggs) is executed before eggs is assigned anything, the local variable eggs doesn’t exist. Python WILL NOT fall back to using the global eggs variable (line 5).”
