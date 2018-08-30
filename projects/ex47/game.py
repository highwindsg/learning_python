class Room(object):     # Create a class named Room with self object params.

    def __init__(self, name, description):  # Define a init function with params self, name
                                            # and description.
        self.name = name    # From self, get the attribute of name and set it to name.
        self.description = description  # From self, get the attribute of description and set
                                        # it to description.
        self.paths = {}     # From self, get the attribute of path and set it to a empty list.

    def go(self, direction):    # Define a go function with params self and direction.
        return self.paths.get(direction, None)

    def add_paths(self, paths):     # Define a add_path function with params self and paths.
        self.paths.update(paths)
