class Scene(object):    # Make a class named Scene that is-a object.

    def enter(self):    # Define a enter function with params self.
        pass


class Engine(object):   # Make a class named Engine that is-a object.

    def __init__(self, scene_map):  # The init function that takes self and scene_map params.
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def nect_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
