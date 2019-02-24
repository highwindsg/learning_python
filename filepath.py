#!/usr/bin/env python3

"""
To avoid problems with your program working across different
operating systems, you should always create file paths using
Python's builtin 'os' module.
"""

import os

# The path function in the os module takes each folder in a
# path as a parameter, and builds the file path for you.
filepath = os.path.join(
"Users",
"mac",
"Documents",
"GitHub",
"learning_python"
)

print(filepath)
