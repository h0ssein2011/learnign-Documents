import numpy as np
from random import  choices
print('Please input 3 numbers!')
#input the lower/upper bounds

a,b,n=map(int,input().split())

population = np.random.randint(low = a, high = b, size =n )
avgs=[]
for i in range(10000):
    avgs.append(np.round(np.mean(choices(population, k=n))))

avgs =sorted(avgs)
print(avgs)

lower_bound =len(avgs) / 100

upprr_bound = len(avgs) / 100
confidence_intervals = avgs[lower_bound , upprr_bound ]
print(confidence_intervals)







