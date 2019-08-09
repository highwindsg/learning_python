#!/usr/bin/env python3

# Remember not to name this file as eg. socket.py or socket1.py as it is like
# re-importing the file you are in.

import socket

# Using the .socket() method from socket module, pass in with two params to connect
# the Internet and socket stream, and assign it to var 'mysock'.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use the .connect() method on var 'mysock', connect to 'data.pr4e.org' on port 80.
mysock.connect(("data.pr4e.org", 80))

# Get the content of the URL txt file with .encode() method in case of any character
# in the content, and assign it to var 'cmd' to be executed.
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()

# Use the .send() method with param of the var 'cmd' on var 'mysock'.
mysock.send(cmd)

while True:
    data = mysock.recv(20)      # Receive the content with 20 bytes per loop using the .recv() method.
    if (len(data) < 1):         # If there are no more content with less than 1 on the length,
        break                   # then break out of the loop.
    print(data.decode(),end="") # Print out the data content with .decode in case of any character set and end it.

mysock.close()  # Then close the 'mysock' var obj.
