#!/usr/bin/env python3

import sqlite3


# From the sqlite3 module, use the .connect() method and parse in the db name, and assign to var conn.
conn = sqlite3.connect("emaildb.sqlite")    # Connect to the db.
# From the conn obj, get the .cursor() method and assign it to the var cur.
cur = conn.cursor() # After connecting to the db, this line is to represent the cursur at the db console.

# If the tablespace Counts exist, then drop the tablespace.
cur.execute("DROP TABLE IF EXISTS Counts")

# Create a new tablespace Counts with email as text and count as integer.
cur.execute('''
            CREATE TABLE Counts (email TEXT, count INTEGER)
            '''
            )

fname = input("Enter file name: ")

if (len(fname) < 1):
    fname = "mbox-short.txt"
    
fh = open(fname)

for line in fh:
    
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email, )) # The '?' is a placeholder to prevent 
    # SQL injection. And the (email, ) is a tuple with one value.
    row = cur.fetchone()    # From obj cur, use the .fetchone() method to get a record and assign to var row.
    
    if row is None:
        cur.execute('''
                    INSERT INTO Counts (email, count)
                    VALUES (?, 1)
                    ''', 
                    (email, )   # A tuple with a single value.
                    )
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email, ))
        
    conn.commit()
    
    
# https://www.sqlite.org/lang_select.html
sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])


cur.close()
print("")
    