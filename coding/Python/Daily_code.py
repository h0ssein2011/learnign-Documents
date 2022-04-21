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




class lift:
    Status ='undefined'
    def __init__(self,f,s):
        self.floor = f
        self.status = s

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'close'
    


lift1 = lift(1,'close')
print(lift1.Status)