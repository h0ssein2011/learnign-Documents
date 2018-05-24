# this is function tutorial

from sys import exit

def gold_room():
    print("this room is full of gold,How much do you want?")

    choice=input(">")
    if "0" in choice or "1" in choice:
        how_much=int(choose)
    else:
        dead("Man ,learn to type a number")

    if how_much <50:
        print("woh you win you are not greedy")
        exit(0)
    else:
        dead("you are a greedy basterd")

def bear_room():
    print("there is a bear here")
    print("the bear has a bunch of honey.")
    print("the fat bear is in front of another door")
    print("How are you going to move bear?")
    bear_moved=False

    while True:
        choice=input(">")

        if choice =="Take honey":
            dead("the bear looks ar the slaps your face")
        elif choice =="taunt bear" and not bear_moved:
            print("the bear hase moved from the door")
            print("you can go trough it now")
            bear_moved = True
        elif choice=="taunt bear" and bear_moved:
            dead("the bear get pissed off and chews your leg")
        elif choice=="open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")
def cthulha_room():
    print("Here you see the grear evil cthulha")
    print("he,itm whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")

    choice  =input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        cthulha_room()

def  dead(why):
    print(why,"good job")
    exit(0)

def start():
    print("you are in a dark room")
    print('there is a door to your righ and left')
    print("which one do you take?")

    choice =input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulha_room()
    else:
        dead("you stumble around the room until you starve")
start()
