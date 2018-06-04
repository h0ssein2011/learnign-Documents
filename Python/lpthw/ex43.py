from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is jot yet confusing.")
        print("subclass it and implement enter().")
        exit(1)

class Engine(object):
    self.scene_map=scene_map

    def play(self):
        current_scene=self.scene_map.opening_scene()
        last_scene=self.scene_map.next_scene('finished')

        while current_scene!= last_scene
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
