import random
credits = 20
bet_amount = 0.20
shapes = ['7','Bar','7-Bar','Bar-7']
win = 0
spins = 10

while credits > 0:
    chance = ['7']
    for i in range(spins):
        credits -= bet_amount
        chance.append(random.choice(shapes))
        print(i, chance)
        if chance.count('7') == 2 :
            credits += 0.40
            chance.append(random.choice(shapes))

            if chance.count('7') == 3 :
                credits += 2.0
                chance.append(random.choice(shapes))

                if chance.count('7') == 4 :
                    credits += 5
                    chance.append(random.choice(shapes))

                    if chance.count('7') == 5 :
                        credits += 15 
                        chance.append(random.choice(shapes))

                        if chance.count('7') == 6 :
                            credits += 50
                            pass
        else :
            chance = ['7']
        print(chance)
        print(credits)
    print('your final credit: ',credits)
        
        


        





