#!/usr/bin/env python3

# https://www.youtube.com/watch?annotation_id=annotation_2243216061&feature=iv&src_vid=Zs8h9kPBfLg&v=F76KGhQG2Xk
import sqlite3

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

# https://www.youtube.com/watch?annotation_id=annotation_606384981&feature=iv&src_vid=F76KGhQG2Xk&v=sRTEsqIctes
def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.4, 'Expert')")
    conn.commit()

#https://www.youtube.com/watch?annotation_id=annotation_3258685183&feature=iv&src_vid=sRTEsqIctes&v=m6HcsJB7ink
def enter_dynamic_data():
    lang = input("What language? ")
    version = float(input("What version? "))
    skill = input("What skill level? ")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, version, skill))

    conn.commit()

#https://www.youtube.com/watch?annotation_id=annotation_511516929&feature=iv&src_vid=m6HcsJB7ink&v=24DczTC9q1E
def read_from_database():

    what_skill = input("What skill level are we looking for? ")
    what_language = input("What language?: ")

    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"

    for row in c.execute(sql, [(what_skill), (what_language)]):
        print(row)
        #print(row[0])



read_from_database()

conn.close()
