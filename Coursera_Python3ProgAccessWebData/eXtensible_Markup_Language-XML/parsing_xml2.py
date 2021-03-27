#!/usr/bin/env python3

""" A triple single quoted 'string' (eg. ''' ... ... ''') in Python is a multi-line 
'string' type.
Below explains how to pull out data from xml.
"""

import xml.etree.cElementTree as ET


input = '''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

print(input)
print("")
print(type(input))
print("")

# Parse the entire xml triple single quoted string 'input' obj into var
# obj 'stuff'.
stuff = ET.fromstring(input)

# From 'stuff', use the .findall() method and parse in all the 'user' in the 
# 'users' tag, and assign to the var 'lst' as a list.
lst = stuff.findall("users/user")
print(lst)
print("")

print("User count:", len(lst))

for item in lst:
    
    # From the item, use the .find() method and parse in the 'name' tag and
    # display it's value by appending the '.text' option. And print out the Name.
    print("Name", item.find("name").text)
    
    # From the item, use the .find() method and parse in the 'id' tag and
    # display it's value by appending the '.text' option. And print out the Id.
    print("Id", item.find("id").text)
    
    # From the item, use the .get() method and parse in the attrib of 'x' 
    # so as to get the value of attrib 'x'. And print out the Attribute.
    print("Attribute", item.get("x"))
    
print("")
