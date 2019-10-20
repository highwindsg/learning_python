#!/usr/bin/env python3

import urllib
from urllib import request
from urllib import parse

# resp = request.urlopen("https://www.google.com/search?q=socratica")
"""
At this point in line 6, if you run the program without commenting, the response will be a 403 forbidden as it is 
not SSL secured. This is to prevent irresponsible use of search request.
To handle a proper SSL site query search, we use eg. https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s
"""

qs = "v=" + "EuC-yVzHhMI" + "&" + "t=" + "5m56s"

# To see what the 'parse' module contains.
print(dir(parse))
print("")

# To create a dict containing the query string params.
params = {"v": "EuC-yVzHhMI", "t": "5m56s"}

# Call the .urlencode' func and pass in the 'params' var obj.
querystring = parse.urlencode(params)

# The result is a string that is suitable for use as the querystring.
print(querystring)
print("")

# Now we can build the URL, and asisgn it to var obj 'url'.
url = "https://www.youtube.com/watch" + "?" + querystring

# Use the .urlopen method from the request module and pass in the url var obj. Then assign to var obj 'resp'.
resp = request.urlopen(url)

# Even if we close the 'resp' var obj, the connection is still open. Therefore our request is fulfilled.
resp.close()
print(resp.code)

# We can then read and decode the server response in a single line.
html = resp.read().decode("utf-8")
# To look at the first 500 char of the html value.
html[:500]
