#!/usr/bin/env python3

import csv      # Import module 'csv' for converting a file object
                # into a csv object.

# Open a new txt file with write permission and assign it to object 'f'.
with open("movies.txt", "w", newline = "") as f:
    w = csv.writer(f, delimiter = ",")  # The writer method from csv module accepts a file
                                        # object and a delimiter as parameters, and assigns
                                        # a csv object back into 'w'.

    w.writerow(["Top Gun",              # The csv object 'w' has a 'writerow' method that
                "Risky Business",       # accepts a list as a param and writes in a row.
                "Minority Report"
                ])

    w.writerow(["Titanic",              # This will write in the second row.
                "The Revenant",
                "Inception"
                ])

    w.writerow(["Training Day",         # This will write in the third row.
                "Man on Fire",
                "Flight"
                ])
