#!/usr/bin/env python3

import os

for folderName, subfolders, filenames in os.walk("//Users/c.yip/Documents/GitHub/learning_python/delicious"):
    print("The current folder is " + folderName)

    for subfolder in subfolders:
        print("SUBFOLDER OF " + folderName + ": " + subfolder)
    for filename in filenames:
        print("FILE INSIDE " + folderName + ": "+ filename)

    print("")