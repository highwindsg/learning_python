class Scene(object):    # Make a class named Scene that is-a object.

    def enter(self):    # Define a enter function with params self.
        pass


class Engine(object):   # Make a class named Engine that is-a object.

    def __init__(self, scene_map):  # The init function that takes self and scene_map params.
        pass

    def play(self):     # Define a play function with a params self.
        pass

class Death(Scene):     # Make a class named Death that is-a Scene.

    def enter(self):    # Define a enter function with a params self.
        pass

class CentralCorridor(Scene):   # Make a class named CentralCorridor that is-a Scene.

    def enter(self):    # Define a enter function with params self.
        pass

class LaserWeaponArmory(Scene):     # Make a class named LaserWeaponArmory that is-a Scene.

    def enter(self):    # Define a enter function with params self.
        pass

class TheBridge(Scene):     # Make a class named TheBridge that is-a Scene.

    def enter(self):    # Define a enter function with params self.
        pass

class EscapePod(Scene):     # Make a class named EscapePod that is-a Scene.

    def enter(self):    # Define a enter function with params self.
        pass


class Map(object):      # Make a class named Map that is-a object.

    def __init__(self, start_scene):    # The function has a init that takes self and start_scene params.
        pass

    def next_scene(self, scene_name):   # The function named next_scene takes self and scene_name params.
        pass

    def opening_scene(self):    # The function named opening_scene takes the self params.
        pass


a_map = Map('central_corridor')     # Set a_map to an instance of class Map that takes params self and 'central_corridor'.
a_game = Engine(a_map)      # Set a_game to an instance of class Engine that takes params self and a_map.
a_game.play()       # From a_game get the play function.
