# import random
# credits = 20
# bet_amount = 0.20
# shapes = ['7','Bar','7-Bar','Bar-7']
# win = 0
# win_lim = 100
# chance = ['7']

# while credits > 0 and credits <= win_lim:
#     credits -= bet_amount
#     chance.append(random.choice(shapes))
#     if chance.count('7') == 2 :
#         credits += 0.40
#         chance.append(random.choice(shapes))

#         if chance.count('7') == 3 :
#             credits += 2.0
#             chance.append(random.choice(shapes))
#         else :
#             chance = ['7']
#             pass

#             if chance.count('7') == 4 :
#                 credits += 5
#                 chance.append(random.choice(shapes))
#             else :
#                 chance = ['7']
#                 pass

#                 if chance.count('7') == 5 :
#                     credits += 15 
#                     chance.append(random.choice(shapes))
#                 else :
#                     chance = ['7']
#                     pass

#                     if chance.count('7') == 6 :
#                         credits += 50
#                         chance = ['7']
#                         pass
#     else :
#         chance = ['7']
#     print('your final credit: ',credits)
        
#https://www.paf.com/en/slots/demo/quickfire?game=seven7sDesktop
import random        
class Seven7s():
    def __init__(self,bet_amount=0.1,balance=100,win_amount = 0,win_limit = 100):
        self.bet_amount = bet_amount
        self.balance = balance
        self.win_amount = win_amount
        self.win_limit = win_limit

    def bet(self,spin=100,shapes=['7','Bar','7-Bar','Bar-7']):
        self.win_amount = 0
        for i in range(spin):
            chance = ['7']
            self.balance -= self.bet_amount
            chance.append(random.choice(shapes))
            if chance.count('7') == 2 :
                print('you win once')
                self.balance += 0.40  
                self.win_amount += 0.40
                chance.append(random.choice(shapes))
                   

                if chance.count('7') == 3 :
                    print('you win twice')
                    self.balance += 2.0 
                    self.win_amount += 2.0 
                    chance.append(random.choice(shapes))


                    if chance.count('7') == 4 :
                        print('you win third time')
                        self.balance += 5.0 
                        self.win_amount += 5.0 
                        chance.append(random.choice(shapes))

                        if chance.count('7') == 5 :
                            print('you win fourth time')
                            self.balance += 15 
                            self.win_amount += 15.0 
                            chance.append(random.choice(shapes))

                            if chance.count('7') == 6 :
                                print('you win fifth time')
                                self.balance += 15
                                self.win_amount += 50.0 
            else:
                print('you lost')                               
        print(self.balance)
        print(self.win_amount)


my_bet = Seven7s()
my_bet.bet()




        

        





