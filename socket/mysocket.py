#!/usr/bin/env python3

import socket

# From socket module, use the .socket() method and parse in the two params of
# Internet and streaming, and assign it to var 'mysock'.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use the .connect() method from 'mysock' var and connect to URL at tcp/80.
mysock.connect( ("data.pr4e.org", 80) )
