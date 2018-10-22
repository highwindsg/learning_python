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

# On each iteration of the 'for loop', a new chunk of 12 characters from
# 'message' is assigned to the variable 'chuck'.
# For eg, on the first iteration, i is 0, and 'chunk' is assigned [0:12],
# which is the string ('Call me at 4').
# And on the next iteration, i is 1, and 'chunk' is assigned message [1:13],
# which is the string ('all me at 41').
for i in range(len(message)):
    chunk = message[i:i+12]

# You pass 'chunk' to 'isPhoneNumber()' to see whether it matches the phone no.
# pattern, and if so you print the chunk.
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)

# The 'for loop' continue to loop through the message, testing each 12-character
# piece and printing any 'chunk' it finds that satisfies 'isPhoneNumber()'.
# Once done going through the 'message', we print 'Done'.
print("Done")

