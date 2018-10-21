#!/usr/bin/env python3
# Finding Patterns of Text Without Regular Expressions.

def isPhoneNumber(text):
    if len(text) != 12:     # Check the string is exactly 12 characters.
        return False
    for i in range(0, 3):   # Check the area code only contains characters.
        if not text[i].isdecimal():
            return False
    if text[3] != "-":      # Check must have first hyphen after the area code. 
        return False
    for i in range(4, 7):   # Check next for 3 more characters.
        if not text[i].isdecimal():
            return False
    if text[7] != "-":      # Check for another hyphen.
        return False
    for i in range(8, 12):  # And finally check for 4 more characters.
        if not text[i].isdecimal():
            return False
    return True             # If the program execution get past all the checks,
                            # then it returns True.

#print("415-555-4242 is a number:")
#print(isPhoneNumber("415-555-4242"))
#print("Moshi moshi is a phone number:")
#print(isPhoneNumber("Moshi moshi"))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print("Done")
