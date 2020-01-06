
import pandas as pd
import numpy as np
address = '~/Lats Win Files/C/python/kaggle-and-other-Online-competitions/human-resources-analytics/HR_comma_sep.csv'
df= pd.read_csv(address)
print(df.shape)

# calculate covariance
def cov_calc(x,y):
    avg_x=np.mean(x)
    avg_y =np.mean(y)

    return (np.sum((x-avg_x) - (y-avg_y)) / (len(x) - 1))

def corr_calc(x,y):

    numinator = cov_calc(x,y)
    denonminator = np.sqrt(np.var(x)) * np.sqrt(np.var(y))
    print(numinator / denonminator)
corr_calc(df['satisfaction_level'] ,df['last_evaluation'])

# it seems the is a positive correlation between satisfacion level and evaluation but it is weak



