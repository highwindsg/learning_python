#!/usr/bin/env python3

# This file needs to be run in a sub-folder my itself.

import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(("data.pr4e.org", 80))
Cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mySock.send(Cmd)

while True:
    data = mySock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end = "")
mySock.close()
