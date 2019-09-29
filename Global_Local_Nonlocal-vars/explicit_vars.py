#!/usr/bin/env python3

def func():
    global x            # Explicitly set the var 'x' as a global var.
    print("1-------", x)    # Therefore print out of 'x' will be 'global'.
    x = "local"             # Assigning a local var 'x' with value of 'local'.
    print("2-------", x)    # Print out the value of var 'x' in the 'func()' which is 'local' because var 'x' has
                            # been re-assigned to a value of 'local'.

x = "global"            # Assign var 'x' with the value of 'global'. This var 'x' is a global var as it is outside
                        # of the 'func()' function.

                        
func()                  # Client call the 'func()' function.
print("3-------", x)    # Print out the value of var 'x' and will be 'local' as line 6 assigns 'x' as 'local' again.
