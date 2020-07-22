#!/usr/bin/env python3

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write("Name, Age, Sport")
outfile.write("\n")
# output each of the rows:
for olympian in olympians:
    row_string = "{}, {}, {}".format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write("\n")
outfile.close()

"""
First, using .format() makes it really clear what we’re doing when we create the 
variable row_string. We are making a comma separated set of values; the {} curly 
braces indicated where to substitute in the actual values. The equivalent string 
concatenation would be very hard to read. An alternative, also clear way to do it 
would be with the .join method: row_string = ','.join(olympian[0], olympian[1], olympian[2]).
Second, unlike the print statement, remember that the .write() method on a file 
object does not automatically insert a newline. Instead, we have to explicitly add 
the character \n at the end of each line.
Third, we have to explicitly refer to each of the elements of olympian when building 
the string to write. Note that just putting .format(olympian) wouldn’t work because 
the interpreter would see only one value (a tuple) when it was expecting three values 
to try to substitute into the string template.
"""
