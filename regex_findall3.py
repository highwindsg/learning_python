#!/usr/bin/env python3

import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good idea.
Namespaces are one honking
great idea -- let's
do more of those!
"""

# The 3rd param 're.MULTILINE' is passed in to
# look for matches on all of the lines in a
# multiline screen or text.
m = re.findall("^If", zen, re.MULTILINE)

print(m)

