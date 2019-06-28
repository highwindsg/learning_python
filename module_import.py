#!/usr/bin/wnv python3

# Importing a manually created module of file converters.py
# that is in the same working dir.
import converters       # Remove file extension in Python syntax.
from converters import kg_to_lbs

# Since the method 'kg_to_lbs' has already been imported from 'converters', we
# can func method call directly and pass in the param 100 to be converted, and
# printed out.
print(kg_to_lbs(100))

# Or alternatively we can just call the attributes of the 'converters' module
# and get the 'kg_to_lbs' method to use.
print(converters.kg_to_lbs(70))

