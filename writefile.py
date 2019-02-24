#!/usr/bin/env python3

st = open("st.txt", "w")    # Open a new file with 'write' permission)
st.write("Hi from Python!") # Actually writes to the file.
st.close()                  # Close the file, or they may cause trouble
                            # left open to other programs or codes.
