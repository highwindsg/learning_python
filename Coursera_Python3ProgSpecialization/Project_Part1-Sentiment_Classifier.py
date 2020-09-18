#!/usr/bin/env python3

"""
We have provided some synthetic (fake, semi-randomly generated) twitter data 
in a csv file named project_twitter_data.csv which has the text of a tweet, 
the number of retweets of that tweet, and the number of replies to that tweet. 
We have also words that express positive sentiment and negative sentiment, in 
the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive 
or negative each tweet is. You will create a csv file, which contains columns 
for the Number of Retweets, Number of Replies, Positive Score (which is how 
many happy words are in the tweet), Negative Score (which is how many angry 
words are in the tweet), and the Net Score for each tweet. At the end, you 
upload the csv file to Excel or Google Sheets, and produce a graph of the Net 
Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, 
a string which represents a word, and removes characters considered punctuation 
from everywhere in the word. (Hint: remember the .replace() method for strings.)
"""

#punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#def strip_punctuation(string):
#    for item in punctuation_chars:
#        string = string.replace(item, '')
#    return string


#string1 = "Today is a good day. However, tomorrow might not be so!"
#new_string1 = strip_punctuation(string1)
#print(new_string1)
#print("")



"""
Next, copy in your strip_punctuation function and define a function called 
get_pos which takes one parameter, a string which represents one or more 
sentences, and calculates how many words in the string are considered positive 
words. Use the list, positive_words to determine what words will count as 
positive. The function should return a positive integer - how many occurrences 
there are of positive words in the text. Note that all of the words in 
positive_words are lower cased, so you’ll need to convert all the words in the 
input string to lower case as well.
"""

#punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

## list of positive words to use
#positive_words = []

#with open("positive_words.txt") as pos_f:
#    for lin in pos_f:
#        if lin[0] != ';' and lin[0] != '\n':
#            positive_words.append(lin.strip())


#def strip_punctuation(string):
#    for item in punctuation_chars:
#        string = string.replace(item, '')
#    return string


#def get_pos(string):
#    pword = strip_punctuation(string).lower()
#    pword = pword.split()
#    count = 0
#    for item in positive_words:
#        if item in pword:
#            count += 1
#    return count


#string2 = "This well acclaimed place is abound with an abundance of accessible fruits."
#new_strings2 = get_pos(string2) 
#print(new_strings2)
#print("")



"""
Next, copy in your strip_punctuation function and define a function called 
get_neg which takes one parameter, a string which represents one or more 
sentences, and calculates how many words in the string are considered negative 
words. Use the list, negative_words to determine what words will count as 
negative. The function should return a positive integer - how many occurrences 
there are of negative words in the text. Note that all of the words in 
negative_words are lower cased, so you’ll need to convert all the words in the 
input string to lower case as well.
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []

with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(string):
    for item in punctuation_chars:
        string = string.replace(item, '')
    return string


def get_pos(string):
    pword = strip_punctuation(string).lower()
    pword = pword.split()
    count = 0
    for item in positive_words:
        if item in pword:
            count += 1
    return count


def get_neg(string):
    nword = strip_punctuation(string).lower()
    nword = nword.split()
    count = 0
    for item in negative_words:
        if item in nword:
            count += 1
    return count
  

string3 = "This 2-faced statue is an abomination and we should abort the purchase."
new_string3 = get_neg(string3)
print(new_string3)
print("")



"""
Finally, copy in your previous functions and write code that opens the file 
project_twitter_data.csv which has the fake generated twitter data (the text 
of a tweet, the number of retweets of that tweet, and the number of replies to 
that tweet). Your task is to build a sentiment classifier, which will detect 
how positive or negative each tweet is. Copy the code from the code windows 
above, and put that in the top of this code window. Now, you will write code 
to create a csv file called resulting_data.csv, which contains the Number of 
Retweets, Number of Replies, Positive Score (which is how many happy words are 
in the tweet), Negative Score (which is how many angry words are in the tweet), 
and the Net Score (how positive or negative the text is overall) for each tweet. 
The file should have those headers in that order. Remember that there is another 
component to this project. You will upload the csv file to Excel or Google 
Sheets and produce a graph of the Net Score vs Number of Retweets. Check 
Coursera for that portion of the assignment, if you’re accessing this textbook 
from Coursera.
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of positive words to use.
positive_words = []

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


# list of negative words to use.
negative_words = []

with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


with open("project_twitter_data.csv", "r") as ofile:
    spam = ofile.read().splitlines()
    spam.pop(0)


outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

myfile = open('project_twitter_data.csv', 'r')
rows = myfile.readlines()[1:]
for line in rows:
    words = line.split()
    numbers = words[-1]
    twrt = numbers.split(',')
    print ('retweets: ', twrt[1], 'replies: ', twrt[2])
    pos_sco = 0
    neg_sco = 0
    for word in words:
        if word in positive_words:
            pos_sco = pos_sco + 1
        if word in negative_words:
            neg_sco = neg_sco + 1
    net_sco = pos_sco - neg_sco
    print ('positive words: ', pos_sco, 'negative words: ', neg_sco, 'Net score: ', net_sco )
    row_string = '{}, {}, {}, {}, {}'.format(twrt[1], twrt[2], pos_sco, neg_sco, net_sco)
    outfile.write(row_string)
    outfile.write('\n')
