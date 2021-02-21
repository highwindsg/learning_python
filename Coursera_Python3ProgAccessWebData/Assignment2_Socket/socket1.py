#!/usr/bin/env python3

import socket


# Just to make a connection to data.pr4e.org on tcp/80.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Connects the socket.
mysock.connect(     # Connect to a server on a tcp port.
    ("data.pr4e.org", 80)
)

# Prepare the message to be sent using a '.encode()' method.
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)    # Actually sending the message.

while True:
    data = mysock.recv(512) # The socket is set to receive data at 512 bytes and assigned to var 'data'.
    if (len(data) < 1): # But if the length of the data values is < 1, which means nothing,
        break   # then program will stop.
    print(data.decode())    # But if there are data values with length > 1, then use the '.decode()' method
    # and print out the data values.
mysock.close()  # Then close the socket connection.

""" The output will show on terminal the first few lines of meta data, and then followed
by the actual data values.

On the Chrome browser, click on View -> Developer -> JavaScript Console.
Then click on the Network tab.
Reload the URL http://data.pr4e.org/romeo.txt and click on the file romeo.txt
and you can see the Headers information in more details. """
