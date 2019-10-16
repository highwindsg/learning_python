#!/usr/bin/env python3

# Remove missing data using the filter func.

countries = ["",
             "Argentina",
             "Brazil",
             "Chile",
             "",
             "Columbia",
             "",
             "Ecuador",
             "",
             "",
             "Venezuela"
             ]

# Using the filter func with first param as None and second param as countries.
# This will filter out the empty strings from the list.
print(
    list(filter(None, countries))
)
