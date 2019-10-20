#!/usr/bin/env python3

"""
In order to use pydoc at the command line with -m option to run as a script:
$ python -m pydoc

To look at the documentation for math:
$ python -m pydoc math

To look at the help text of a class, such as tuple:
$ python -m pydoc tuple

Or to look at a function like pow:
$ python -m pydoc pow

To search pydoc module for the keyword 'ftp':
$ python -m pydoc -k ftp

To use pydoc to learn more of the ftplib class:
$ python -m pydoc ftplib
The output will also show some examples on how to use the ftplib.

To check if pydoc contains any document on the keyword sql.
$ python -m pydoc -k sql

To read on the sqlite3 package.
$ python -m pydoc sqlite3

Can also start a http port to browse the documentation on a browser.
$ python -m pydoc -p 314
Then press [b] and will launch the default browser.
Press [q] will stop the server.

Alternatively can quickly start pydoc with option -b to start an HTTP server on a available random port,
and launch a browser.
$ python -m pydoc -b

Can also use pydoc to generate html files for documentation either store locally or on a remote server.
Eg. create a subfolder 'pydoc-demo'.
~/pydoc-demo $ python -m pydoc -w json
This will write a json.html documentation file in the sub-folder.
"""
