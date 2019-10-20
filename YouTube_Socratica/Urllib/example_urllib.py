#!/usr/bin/env python3

"""
The urllib library comes with 5 module packages.
request:    for opening URLs.
response:   used internally by the request module, will not need to work with this module directly.
error:      request exceptions
parse:      a variety of useful parse modules for breaking up a URL into meaningful pieces,
            eg. scheme, host, port, query string data.
robotparser:    robots.txt files, just for checking robots.txt files for what permissions are granted
                bots and crawlers.
"""

import urllib

print(dir(urllib))
print("")

from urllib import request

print(dir(request))
print("")

# From the request module, use the .urlopen method and pass in the URL of wikipedia.org, then assign it to var 'resp'.
resp = request.urlopen("https://www.wikipedia.org")
print(type(resp))   # Print out the data type of var 'resp'.
print("")

# To see what can be done with the 'resp' var, use the dir() method.
print(dir(resp))
print("")

# To test if the var obj 'resp' (the wikipedia URL) does response well as a request, use the .code method.
# If the return response code is 200, then it is successful.
print(resp.code)
print("")

# To see how large the response is in bytes, use the .length method.
print(resp.length)
print("")

# To use the .peek func to look at a small part of the response, rather than the full value or page.
# And if the response starts with a b' then it means the URL starts with a bytes object.
print(resp.peek())
print("")

# Read the entire 'resp' var obj, using the .read() func.
data = resp.read()
print(type(data))   # Print out the type of data class of var 'data'.
print(len(data))    # This will show that it is the correct same length size as in line 39.
print("")

# In order to decode the bytes obj to html txt, call the 'decode' method and specify the encoding that was used.
# To check what encoding type was used, use the .peek() func previously.
html = data.decode("UTF-8")
print(type(html))   # Check the data type of var 'html' and can see that we have a string data type.
print(html)     # Print out the value of var obj 'html', which is the entire web page in txt.
print("")

# If you try to read the response 'resp' again, there will be nothing as Python closes the connection once it has
# read before. Then must use the .urlopen() method to request again.
print(resp.read())
print("")
