import numpy as np
from random import choices
print('Please input 3 numbers!')
#input the lower/upper bounds

a,b,n = map(int,input().split())
pop = np.random.randint(a,b,n)
avgs=[]
for i in range(10000):
    avgs.append(np.mean(choices(pop , k= n)))

print(avgs)
print('standard error is :'.format(np.std(avgs)))

