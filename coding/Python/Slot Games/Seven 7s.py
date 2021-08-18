import random
credits = 20
bet_amount = 0.20
shapes = ['7','Bar','7-Bar','Bar-7']
win = 0
win_lim = 100
chance = ['7']

while credits > 0 and credits <= win_lim:
    credits -= bet_amount
    chance.append(random.choice(shapes))
    if chance.count('7') == 2 :
        credits += 0.40
        chance.append(random.choice(shapes))

        if chance.count('7') == 3 :
            credits += 2.0
            chance.append(random.choice(shapes))
        else :
            chance = ['7']
            pass

            if chance.count('7') == 4 :
                credits += 5
                chance.append(random.choice(shapes))
            else :
                chance = ['7']
                pass

                if chance.count('7') == 5 :
                    credits += 15 
                    chance.append(random.choice(shapes))
                else :
                    chance = ['7']
                    pass

                    if chance.count('7') == 6 :
                        credits += 50
                        chance = ['7']
                        pass
    else :
        chance = ['7']
    print('your final credit: ',credits)
        
        


        





