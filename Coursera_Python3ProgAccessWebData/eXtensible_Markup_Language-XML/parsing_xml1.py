#!/usr/bin/env python3

import xml.etree.ElementTree as ET


""" A triple quoted string (eg. ''' ... ... ''') in Python is a multi-line string.
Below explains how to pull out data from xml.
"""

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

# Using ET.fromstring() method, parse in var obj 'data', and assign the xml triple
# quoted string to var 'tree'.
tree = ET.fromstring(data)

# From var obj 'tree' use the .find() method and parse in the 'name' tag and
# get it's text by appending '.text'. And then print it out.
print("Name:", tree.find("name").text)

# From var obj 'tree' use the .find() method and parse in the 'phone' tag and
# display it's type value by using the '.get()' method. And then print it out.
print(tree.find("phone").get("type"))
print("phone:", tree.find("phone").text)

# From var obj 'tree' use the .find() method and parse in the 'email' tag and
# display the attrib of 'hide' by appending '.get()' method parse in 'hide'.
print("Email hidden?:", tree.find("email").get("hide"))
print("")
