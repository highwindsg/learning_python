#!/usr/bin/env python3

"""
Many Students in Many Courses.

Instructions:
This application will read roster data in JSON format, parse the file, and then produce an 
SQLite database that contains a User table, Course table, and Member table and then populate the 
tables from the data file in 'roster_data.json'.
"""


import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some database tables setup.
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:  # This is to assume that the json file is already
    fname = 'roster_data.json'  # located in the same folder as the
    # *.py application file.

# A few sample line of the JSON file below.
#[
#  [
#    "Eisha",
#    "si110",
#    1
#  ],
  
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role) )

    conn.commit()

print("")


"""
Once you have made the necessary changes to the program and it has been run successfully reading 
the above JSON data, run the following SQL command:

sqlstr='SELECT User.name,Course.title, Member.role FROM User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2'

The output should look as follows:
Zoe|si206|0
Zara|si110|0

Once that query gives the correct data, run this query:

sqlstr='SELECT "XYZZY" || hex(User.name || Course.title || Member.role ) AS X FROM User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id ORDER BY X LIMIT 1'

You should get one row with a string that looks like: XYZZY53656C696E613333.
"""
