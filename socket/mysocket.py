#!/usr/bin/env python3

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ("data.pr4e.org", 80) )
