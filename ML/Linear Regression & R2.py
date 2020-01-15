from random import choices

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('/home/hossein/Lats Win Files/C/python/kaggle-and-other-Online-competitions/Ames Housing dataset/Input/train.csv')
int_cols =[col for col in df.columns if df[col].dtype in ('int64','float64')]

print(int_cols)

#use univariate regression
X=pd.DataFrame(df['LotArea'])
y=pd.DataFrame(df['SalePrice'])

X_train,X_valid, y_train,y_valid = train_test_split(X,y,train_size =0.8 , random_state =0)


lm = LinearRegression()
lm.fit(X_train,y_train)

print(lm.coef_,lm.intercept_)
print(lm._residues)

print()
