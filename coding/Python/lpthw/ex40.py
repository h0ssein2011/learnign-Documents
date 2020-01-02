#this is first class tutorial

class song(object):

    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday=song(['happy birhtday to you','I hope you will get soon','we will be married soon'])

balls_on_brage=song(['I have a ball','I love it too much','my daady give it to me'])

happy_bday.sing_me_a_song()
balls_on_brage.sing_me_a_song()
