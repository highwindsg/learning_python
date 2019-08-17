#!/usr/bin/env python3

# Import sqlite3 library module.
import sqlite3

# Use the .connect() method from sqlite3 module and pass in param of the filename 'emaildb.sqlite', and assign
# it to var 'conn'.
conn = sqlite3.connect("emaildb.sqlite")

# Use the .cursor() method from var obj 'conn', and assign to var 'cur', and can read as current db file.
cur = conn.cursor()

# Use the .execute() method from var obj 'cur' to issue SQL statement to firstly drop the table 'Counts'
# if it already exist. If table 'Counts' does not exists, then it is ok, and the program will move on.
cur.execute("DROP TABLE IF EXISTS Counts")

# Use the .execute() method from var obj 'cur' to issue SQL statement to create the tablespace 'Counts',
# with email as TEXT datatype, and count as INTEGER datatype.
cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

# Ask user to enter the filename, if not then use the hard coded default, and assign to var 'fname'.
fname = input("Enter file name (or press Enter for default 'mbox-short.txt'): ")
if (len(fname) < 1): fname = "mbox-short.txt"

fh = open(fname)    # Use the open() func and pass in the 'fname' var,
                    # and assign it to var 'fh' (read as file-in-hand).
for line in fh:
    if not line.startswith("From: "):   # Only for every line in 'fh' that starts with 'From: ',
        continue                        # then can proceed.
    pieces = line.split()   # Split the line that starts with 'From: ' into indexes and assign to var 'pieces'.
    email = pieces[1]       # Take the second index from 'pieces' var, [0] is first, [1] is second,
                            # and assign the second index (which is the email address) to var 'email'.
    # Use the .execute() method from var obj 'cur' to issue SQL select statement to find out how many
    # times a email address has been repeated that starts with 'From: '.
    # The '?' syntax is to prevent against SQL-injection hacking attempt, and the tuple '(email,)' will be the
    # actual email that will be parsed into '?' to complete the SQL select statement execution.
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email,))

    # Use the .fetchone() func from the var obj 'cur' to grab the first one and assign to var 'row'.
    row = cur.fetchone()
    if row is None:     # If row is blank, then issue SQL statement to INSERT the email address and count.
        cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email,))
    else:               # If row exist with the same email, then issue SQL statement to UPDATE Counts by adding 1.
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email,))
    conn.commit()       # Use the .commit() method on the sqlite3 db file to save the changes.

# https://www.sqlite.org/lang_select.html
# Select out the 'email' and 'count' column from the 'Counts' tablespace and sort then in descending order,
# and limit to only 10. Then assign the result of the select statement to var 'sqlstr'.
sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

# Use the .execute() method frmo 'cur' obj var and parse in the param of var 'sqlstr'.
for row in cur.execute(sqlstr):     # So that for every row in the select statement,
    print(str(row[0]), row[1])      # print out the email column from first index, and the count column
                                    # from the second index, in string type.

cur.close()     # Finally use the .close() method on var obj 'cur' db file, to close the opened db file.
