#!/usr/bin/env python3

# Import the regular express module 're'.
import re

# Prepare a short paragraph with missings words
# with hints of what to fill in later, and assign
# it to var 'text'.
text =  """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest time. The
 giraffee is the tallest of all
 living __PLURAL_NOUN__, but
 scientists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffe's tremendous height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 it legs and __BODYPART__.
 """

# Define a function named 'mad_libs()' with param mls.
def mad_libs(mls):  # 'mls' just meant 'mad libs strings'.
    """
    :param mls: String
    with parts the user
    should fill out surrounded
    by double underscores.
    Underscores cannot
    be inside hint e.g., no
    __hint_hint__ only
    __hint__.
    """

    """
    Use the findall() method in to match on the first
    double underscore and the last underscore with .*?
    in between, and then to match them in the second
    param of 'mls'.
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
            print("\n")
            mls = mls.replace("\n", "")
            print(mls)
    else:
        print("invalid mls")

# Call the mad_libs() method on 'text'.
mad_libs(text)

