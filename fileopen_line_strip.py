#!/usr/bin/env python3

fname = input("Enter filename: ")
if len(fname) < 1:          # This line is so that if user just press ENTER,
    fname = "clown.txt"     # the program will take the default 'clown.txt' file as entered.
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
    print(line)         # This will print out the entire line of the txt file with right empty space removed.
    words = line.split()
    print(words)        # This will print pout the line separated by a comma word by word in a list.
    for word in words:  # This will print out individual word in a column, one word per line.
        print(word)
        if word in dic:
            dic[word] = dic[word] + 1
            print("**Existing**")
        else:
            dic[word] = 1
            print("**NEW**")
        print(dic[word])

print(dic)

# To find out the most common word.
for k, v in dic.items():    # So instead of printing out in a dict line, we print out the key and value
    print(k, v)             # in a column.
