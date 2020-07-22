#!/usr/bin/env python3

fileconnection = open("olympics.txt", "r")
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(",")
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(",")
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))

"""
In the above code, we open the file, olympics.txt, which contains data on some olympians. 
The contents are similar to our previous olympics file, but include an extra column with 
information about medals they won.
We split the first row to get the field names. We split other rows to get values. Note that 
we specify to split on commas by passing that as a parameter. Also note that we first pass 
the row through the .strip() method to get rid of the trailing n.
Once we have parsed the lines into their separate values, we can use those values in the 
program. For example, in the code above, we select only those rows where the olympian won 
a medal, and we print out only three of the fields, in a different format.
Note that the trick of splitting the text for each row based on the presence of commas only 
works because commas are not used in any of the field values. Suppose that some of our events 
were more specific, and used commas. For example, “Swimming, 100M Freestyle”. How will a 
program processing a .csv file know when a comma is separating columns, and when it is just 
part of the text string giving a value within a column?
The CSV format is actually a little more general than we have described and has a couple of 
solutions for that problem. One alternative format uses a different column separator, such 
as | or a tab (t). Sometimes, when a tab is used, the format is called tsv, for tab-separated 
values). If you get a file using a different separator, you can just call 
the .split('|') or .split('\\t').
"""
