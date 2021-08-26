import random
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Heart','Diamond','Spade','Clubs']
values ={'2':2,'3':3,'4':4,'5':5,'6':6,
            '7':7,'8':8,'9':9,'10':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
Deck = []
for suit in suits:
    for rank in ranks:
        Deck.append((suit,rank)) 
print(len(Deck))
random.shuffle(Deck)
Player1_Deck = []
Player2_Deck = []
for i in range(26):
    Player1_Deck.append(Deck.pop(0))
    Player2_Deck.append(Deck.pop(0))
print(Player1_Deck)
print('*'*60)
print(Player2_Deck)

player1_score = 0
player2_score = 0
for i in range(26):
    if values[Player1_Deck[i][1]] >  values[Player2_Deck[i][1]]: 
        player1_score += 1    
    elif values[Player1_Deck[i][1]] <  values[Player2_Deck[i][1]]: 
        player2_score += 1 
    else:
        pass
print('Player1_Score : ',player1_score)
print('Player2_Score : ',player2_score)










