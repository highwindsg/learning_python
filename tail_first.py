def tail(self):
    return self[1:]

letters = ["a", "b", "c"]
rest = tail(letters)
print(rest)

# 'tail' returns all except the first elements of a list.
# This function leaves the original list unmodified.
