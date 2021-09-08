import random
suits =['Diamond','Spades','Heart','Clubs']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values ={ 'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7
            ,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
# card class
""" Add a Card class to represent the differnet cards"""
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
my_card = Card('Diamond','Eight')
print(my_card)


# deck class
class Deck():
    def __init__(self):
        self.All_cards =[]
        for suit in suits :
            for rank in ranks:
                self.All_cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.All_cards)

    def deal_one(self):
        self.All_cards.pop()

# This_Deck = Deck()
# This_Deck.shuffle()
# for card in This_Deck.All_cards:
#     print(card)

# Player class
class Player():
    def __init__(self,name):
        self.name = name
        self.All_cards = []
    
    def remove(self):
        return self.All_cards.pop(0)
    
    def add_card(self,new_card):
        if type(new_card) == type([]):
            
            return self.All_cards.extend(new_card)
        else:
            return self.All_cards.append(new_card)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.All_cards)} cards'
    
# Ali = Player('Ali')
# print(Ali)
# king_Ace = Card('Diamonds','King')
# Two_clubs = Card('Clubs','Two')
# Ali.add_card([king_Ace,Two_clubs])
# print(Ali)

# lets begin the game
this_Deck = Deck()
this_Deck.shuffle()

Player_1 = Player('Ali')
Player_2 = Player('Reza')

for i in range(26):
    Player_1.add_card(this_Deck.deal_one())
    Player_2.add_card(this_Deck.deal_one())
print(Player_1)
print(Player_2)

Game_on = True 
while Game_on:
    if len(Player_1.All_cards) == 0:
        print(f'{Player_1.name} is lost and {Player_2.name} wone the game')
        Game_on = False
        break  

    if len(Player_2.All_cards) == 0:
        print(f'{Player_2.name} is lost and {Player_1.name} wone the game')
        Game_on = False
        break


    at_war = True
    while at_war:
        Player_1_cards = []
        Player_1_cards.append(Player_1.remove())
        print(Player_1.remove())

        Player_2_cards = []
        Player_2_cards.append(Player_2.remove()) 
        print(Player_2_cards)


        if Player_1_cards[-1].value > Player_2_cards[-1].value :
            Player_1.add_card(Player_1_cards)
            Player_1.add_card(Player_2_cards)
            at_war = False
        
        if Player_1_cards[-1].value < Player_2_cards[-1].value :
            Player_2.add_card(Player_1_cards)
            Player_2.add_card(Player_2_cards)
            at_war = False
    
        



