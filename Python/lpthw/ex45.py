from random import randint
rooms=['dark_room','gold_room','rand_room','win_room']

class dark_room(object):
    def enter():
        print("start dark_room")

class gold_room(object):
    def get_gold():
        print("hey you get golds")
        return "Finished you win"

class rand_room(object):
    def choose():
        which_room=int(input("choose number between 0 and 3:"))
        if which_room ==2 :
            which_room=int(randint(0,3))
        else:
            return rooms[which_room]

class win_room(object):
    def win():
        print("Hey you win you can earn money!")

which_room=int(input("choose number between 0 and 3:"))
if which_room == 0:
    dark_room.enter()
elif which_room == 1:
    gold_room.get_gold()
elif which_room == 2:
    rand_room.choose()
else:
    win_room.win()
