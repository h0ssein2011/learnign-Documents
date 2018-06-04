from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is jot yet confusing.")
        print("subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map

    def play(self):
        current_scene=self.scene_map.opening_scene()
        last_scene=self.scene_map.next_scene('finished')

        while current_scene!= last_scene:
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene)

        #be sure to print ut the last scene_map
        current_scene.enter()


class Death(Scene):
    quips=[
            "you died.you kinda suck at this.",
            "your mother would bbe proud ... if she were smarter.",
            "such a luser.",
            "I have a small puppy that's better at this",
            "you are worse than Dad's jokes"
    ]


    def enter(self):
        peint(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
                 the Gothons of planet """
                 ))
        action=input(">")

        if action == "shoot!":
            print(dedent(""" quick on the draw """))
            return 'death'

        elif action =="dodge!":
            print(dedent(""" Like the worl class boxer """))
            return 'death'

        elif action =='tell a joke':
            print(dedent("""Lucky for you they made"""))
            return 'laser_weapon_armory'
        else:
            print("Does not compute")
            return 'centtral_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""you do a drive roll into the weapon Armory """))

        code = "{}{}{}".format(randint(1,9),randint(1,9),randint(1,9))
        guess=input("[Keypad]>")
        guesses=0

        while guess != code and guesses <10:
            print("BZZZZDDD!")
            guesses+=1
            guess=input("[keypad]>")

        if guess == code:
            print(dedent("""the container clicks open and the seal ... """))
            return 'the_bridge'

        else:
            print(dedent(""" the lcoj buzzes one last time and then ..."""))
        return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""your burst onto the bridge with the netron """))

        action =input(">")
        if action ==  'throw the bomb':
            print(dedent(""" in a panic you throw the bomb ....""" ))
            return 'death'

        elif action == 'slowly place the bomb':
            print(dedent("""you point your blaster at the bomb under the ... """))
            return 'escape_pod'
        else:
            print("Does not compute!")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""you rush through the ship deseprately trying the.... """))
        good_pod=randint(1,5)
        guess=input("[pod #]>")

        if int(guess) !=good_pod:
            print(dedent(""" you jump into pod {guess} and hit the """))
            return 'death'
        else:
            print(dedent(""" you jump into {guess}...."""))
        return 'finished'

class Finished(Scene):
    def enter(self):
        print('you won! good job')
        return 'finished'


class Map(object):
    Scenes={

    'centeral_corridor':CentralCorridor(),
    'laser_weapon_armory':LaserWeaponArmory(),
    'the_bridge':TheBridge(),
    'escape_pod':EscapePod(),
    'death':Death(),
    'finished':Finished(),

    }

    def __init__(self,start_scene):
        self.start_scene=start_scene

    def next_scene(self,scene_name):
        val=Map.Scenes.ger(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(start_scene)



a_map=Map('centeral_corridor')
a_game=Engine(a_map)
a_game.play()
