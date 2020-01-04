

import pandas as pd
import numpy as np
address = '~/Lats Win Files/C/python/kaggle-and-other-Online-competitions/human-resources-analytics/HR_comma_sep.csv'
df= pd.read_csv(address)
print(df.shape)

# calculate covariance
def cov_calc(x,y):
    avg_x=np.mean(x)
    avg_y =np.mean(y)

    print (np.sum((x-avg_x) - (y-avg_y)) / (len(x) - 1))


cov_calc(df['satisfaction_level'] ,df['last_evaluation'] )
# it seems the is a positive relation between satisfacion level and evaluation


cov_calc(df['satisfaction_level'] ,df['average_montly_hours'])


