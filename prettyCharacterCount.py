import pprint    # The 'pprint' library makes the output more cleaner.

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)    # The 'pprint.pprint() function is helpful when
                        # the dictionary itself contains nested lists or
                        # dictionaries.
#print(pprint.pformat(count))

