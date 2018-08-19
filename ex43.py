from sys import exit
from random import randint
from textwrap import dedent     # This little function helps write our rooms descriptions
                                # using """ (triple-quote) strings. It strips leading white-spaces
                                # from the beginnings of lines in a string.

class Scene(object):    # Make a class named Scene that is-a object.

    def enter(self):    # Define a enter function with params self.
        print("This scene is not not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):   # Make a class named Engine that is-a object.

    def __init__(self, scene_map):  # The init function that takes self and scene_map params.
        self.scene_map = scene_map 

    def play(self):     # Define a play function with a params self.
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):     # Make a class named Death that is-a Scene.

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a looser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."

    ]

    def enter(self):    # Define a enter function with a params self.
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):   # Make a class named CentralCorridor that is-a Scene.

    def enter(self):    # Define a enter function with params self.
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the new Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
               Quick on the draw you yank out your blaster and fire
               it at the Gothon. His clown costume is flowing and
               moving around his body, which throws off your aim.
               Your laser hits his costume but misses him entirely.
               This completely ruins his brand new costume his mother
               bought him, which makes him fly into an insane rage
               and blast you repeatly in the face until you are
               dead. Then he eats you.
               """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out. You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


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
