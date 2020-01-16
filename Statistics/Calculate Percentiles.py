import numpy as np 
from random import choices

dataset= np.random.randint(1,1000,40)

dataset = list(set(dataset))
dataset=sorted(dataset)

def percentiles(x):

    ln=len(x)
    q1=x[int(ln*1/4)]
    q2=x[int(ln*2/4)]
    q3=x[int(ln*3/4)]
    return q1,q2,q3

print('percentiles dataset are:',percentiles(dataset))