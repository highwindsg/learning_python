#!/usr/bin/env python3

import socket

"""
    Python Strings to Bytes
    =======================
    1. When we talk to an external resource like a network socket se sends bytes,
    so we need to encode Python 3 strings into a given character encoding.
    2. When we read data from an external resource, we must decode it based on
    the character set so it is properly represented in Python3 as a string.
"""

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Connects the socket.
mysock.connect(     # Connect to a server on a tcp port.
    ("data.pr4e.org", 80)
)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode()
    print(mystring)

