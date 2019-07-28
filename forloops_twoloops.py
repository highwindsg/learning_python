#!/usr/bin/env python3

friends = ["Joseph", "Glenn", "Sally"]

for name in friends:
    print("Happy New Year:", name)

print("")

# Another way is to put the friends list in a range and use the
# for loop to iterate the name in the friends list.
for i in range(len(friends)):
    name = friends[i]
    print("Happy New Year:", name)
