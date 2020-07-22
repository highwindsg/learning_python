#!/usr/bin/env python3

olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name", "Age", "Sport"')
outfile.write("\n")
# outfile each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write("\n")
outfile.close()

"""
As described previously, if one or more columns contain text, and that text could contain 
commas, we need to do something to distinguish a comma in the text from a comma that is 
separating different values (cells in the table). If we want to enclose each value in 
double quotes, it can start to get a little tricky, because we will need to have the double 
quote character inside the string output. But it is doable. Indeed, one reason Python 
allows strings to be delimited with either single quotes or double quotes is so that one 
can be used to delimit the string and the other can be a character in the string. 
If you get to the point where you need to quote all of the values, we recommend learning 
to use python’s csv module.
"""
