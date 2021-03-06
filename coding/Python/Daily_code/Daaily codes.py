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



# day_2


