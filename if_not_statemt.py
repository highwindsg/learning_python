#!/usr/bin/python3

"""
if applicant has high income OR good credit
    Eligible for loan
if applicant has good credit AND doesn't have a criminal record
    Eligible for loan
"""

# Change the boolean condition from True to False and run the program again.
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:     # 'and not' is a logical operator.
    print("Eligible for loan")

"""
AND: if both boolean values are True; if both boolean values are False
OR: at least one boolean value is True
NOT: inverses the boolean value
"""

