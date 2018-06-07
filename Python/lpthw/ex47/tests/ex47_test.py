from nose.tools import *
from ex47.game import Room

def test_room():
    gold=Room("Gold Room",""" this room has gold in it you can grab """)
    assert_equal(gold.name,"GoldRoom")
    assert_equal(gold.paths,{})

def test_room_paths():
    center=Room("Center","test room un the center")
    north=Room("Center","test room un the North")
    south=Room("Center","test room un the center")

    center.add_paths({'north':north , 'south':south})
    assert_equal(center.go('north'),north)
    assert_equal(center.go('south'),south)

def test_map():
    start=Room("Start",'you can go west and down a hole')
    west=Room("Trees","ther are trees here you can go")
    down=Room("Dungeon","It's dark down here you can go")

    start.add_paths({'west':west,'down':down})
    west.add_paths({'east':start})
    down.add_paths({'up':start})

    assert_equal(start.go('west'),west)
    assert_equal(start.go('west'),west).go('east'),start)
    assert_equal(start.go('down').go('up'),start)
