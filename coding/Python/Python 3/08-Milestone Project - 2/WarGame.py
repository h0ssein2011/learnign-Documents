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
    def suffle(self):
        random.shuffle(self.All_cards)

    def deal_one(self):
        self.All_cards.pop()

This_Deck = Deck()
This_Deck.suffle()
for card in This_Deck.All_cards:
    print(card)

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
    
Ali = Player('Ali')
print(Ali)



# setup