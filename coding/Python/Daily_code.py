# daily_code
# day1
# cross_validation
rom sklearn.linear_model import LogisticRegression
import  pandas as pd
from sklearn.metrics import  accuracy_score


def cross_val(df,cv=10):
    models = {'LR':LogisticRegression()}
    jumps = df.shape[0] // cv

    scores=[]

    start=0
    for row in range(0,df.shape[0],jumps):

        train_set=pd.DataFrame()
        test_set=pd.DataFrame()
        test_set = test_set.append(df.iloc[start:start + jumps,:])
        train_set =df.iloc[~test_set.index]


        model = models['LR']
        fited_model= model.fit(train_set)
        pred=fited_model.predict((test_set))
        scores.append(accuracy_score(pred,y_test))

        del train_set, test_set 
        start+=jumps



# introduce new way of learing code by doing 
# so pulblicy commitment to do daily code every day in python

#D1


game =[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
def game_board():
    print('a , b ,c ')
    for count , row in enumerate(game):
        print(count ,row) 

game_board()

game[0][1] = 2
game_board()

# Global vs local
x = 1
def test():
    x = 2
test()
print(x)


x = 1
def test():
    global x
    x = 2
test()
print(x)


x = [1]
def test():
    x = [2]
test()
print(x)


x = [1]
def test():
    global x
    x = [2]
test()
print(x)


x = [1]
def test():
    x[0] = 2
test()
print(x)


game =[[1,2,0],
       [0,1,0],
       [2,0,3]]

diags=[]
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)

diags=[]
for col , row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])
print(diags)



def game_board(game_map , player=0,row=0,column=0 , just_display=False):
    if not just_display:
        game_map[row][column] = player
    for count , row in enumerate(game_map):
        print(count, row)
    return game_map

game_board(game,player=1)




def Poki_game(l):
    played =[]
    num_shots = len(l)-1
    for i in range(num_shots):
        shot = int(input('select a Poki'))
        if shot in played or shot not in l:
            print('You lost!....')
            break
        else:
            played.append(shot)

    if len(played)+1 == len(l):
        print('you won')

Poki_game([1,5,6,8,9])

import random
def Memory_Match(num_games=5):
    ls= random.sample(range(0,100), num_games)
    score=0
    
    for i in range(num_games):
        init=random.choice(ls)
        print(init)
        last_num=int(input('what was the last number? '))
        if last_num == init:
            score+=1
    print('your score is {} out of {}'.format(score,num_games)) 

Memory_Match(5)

