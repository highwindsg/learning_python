#!/usr/bin/env python3

fname = input("Enter filename: ")
if len(fname) < 1:          # This line is so that if user just press ENTER,
    fname = "clown.txt"     # the program will take the default 'clown.txt' file as entered.
hand = open(fname)

dic = dict()
for line in hand:
    line = line.rstrip()
#    print(line)         # This will print out the entire line of the txt file with right empty space removed.
    words = line.split()
#    print(words)        # This will print pout the line separated by a comma word by word in a list.
    for word in words:  # This will print out individual word in a column, one word per line.
#        print(word)
        # common idiom to retrieve/create/update counter.
        dic[word] = dic.get(word, 0) + 1

print(dic)

tmp = list()

for k, v in dic.items():
    # print(k, v)
    newtuple = (v, k)
    tmp.append(newtuple)

print("Flipped", tmp)

tmp = sorted(tmp, reverse = True)
print("Sorted", tmp[:5])    # Only print out the top 5 sorted from the 'tmp' list.

for v, k in tmp[:5]:    # This forloop will print out the top 5 words that are used
    print(k, v)         # most and the number of times it occurred.
