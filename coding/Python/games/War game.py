ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Heart','Diamond','Spade','Clubs']
Combs = []
for suit in suits:
    for rank in ranks:
        Combs.append((suit,rank)) 
print(Combs)
print(len(Combs))

