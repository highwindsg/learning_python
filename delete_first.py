def delete_first(self):     # Create a function named delete_first with parm self.
    del self[0]             # Delete the first index of the parm self.

letters = ["a", "b", "c"]
delete_first(letters)       # Passing the variable letters of list to the function.
print(letters)

# When you pass a list to a function, the function gets a reference to the list.
# If the function modifies a list parameter, the caller sees the change.
# Therefore 'delete_first' removes the first element from the list.
