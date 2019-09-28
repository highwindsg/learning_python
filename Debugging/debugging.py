#!/usr/bin/env python3

""" 'pdb' is a command line tool for debugging Python script. """

def add(x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    x = input("Num 1 : ")       # The int() method is purposely omitted out in order to show how to use debugging.
    y = input("Num 2 : ")       # The int() method is purposely omitted out in order to show how to use debugging.
    z = add(x, y)
    print(z)

"""
The program above will show a concatenation result instead of an addition result. So we use debugging to find out why.
Open a cmd line window and go to the folder of this python file.
Type $ 'python3 -m pdb debugging.py' to start the python debugging mode.
In the (Pdb) mode, there are some options you can use.
(Pdb) help      # This will show the all options available. eg. (Pdb) help where.
(Pdb) where     # This will show the current current absolute path to the python file.
(Pdb) next      # or in short 'n' will 'show' the next line in the code.
(Pdb) continue  # or in short 'c' will 'execute' the command of the next line. eg. if line next line is an input line.
(Pdb) whatis    # After the input into a var, can use the 'whatis' command to check what is the data type of the var.
(Pdb) step      # This option allows the debugging to step into the function or a class.
(Pdb) break     # Can use the break point eg. in line 12. eg. (Pdb) break 12. Then use the 'continue' to proceed.
                # eg. (Pdb) break 13. This will set a break point from line 13. And then press 'c' or 'continue' to
                # next line to input the number. After the two input finishes, pdb will stops at line 13.
(Pdb) q         # To quit and exit out of the debugging mode.
"""