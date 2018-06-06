# import needed library
from random import randint
#choose rooms before start
rooms=['dark_room','gold_room','rand_room','win_room']

#Dark Room is the first
class DarkRoom(object):
    def enter():
        print("start dark_room")
#gold room that finished room
class GoldRoom(object):
    def get_gold():
        print("hey you get golds")
        return "Finished you win"
#this is just a fake room that pass you another room! haha
class RandRoom(object):
    def choose():
        which_room=int(input("choose number between 0 and 3:"))
        if which_room ==2 :
            which_room=int(randint(0,3))
        else:
            return rooms[which_room]
# this is the last room
class WinRoom(object):
    def win():
        print("Hey you win you can earn money!")

#let's play
which_room=int(input("choose number between 0 and 3:"))
if which_room == 0:
    DarkRoom.enter()
elif which_room == 1:
    GoldRoom.get_gold()
elif which_room == 2:
    RandRoom.choose()
else:
    WinRoom.win()
