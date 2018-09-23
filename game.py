class Room(object):     # Make a class named Room with its own self object.

    def __init__(self, name, description):  # Define a init function with self, name and description parms.
        self.name = name        # From self, get the name attribute and assign it to name.
        self.description = description      # From self, get the description attribute and assign it to description.
        self.paths = {}         # From self, get the paths attribute and assign it to an empty list.

    def go(self, direction):    # Define a function named go with self and direction params.
        return self.paths.get(direction, None)

    def add_paths(self, paths):     # Define a function named add_paths with self and paths params.
        self.paths.update(paths)
