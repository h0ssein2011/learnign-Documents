import numpy as np 
from random import choices
import math

items = ['ornage','grape']

n=int(input('please entere the number of items:'))

selection = choices(items ,k=n)
print(selection)

def binoial_dist(n,x,p=0.5):
    numerator = math.factorial(n)
    denominator = (math.factorial(n) * math.factorial(n-x))
    num_combinations = numerator / denominator
    pr_x = p ** x
    pr_1_x =p **(1-x)
    return  round(num_combinations * pr_x * pr_1_x,4)

num_oranges=selection.count('ornage')
grapes = n -orages
print('the probaility of chosing {} in {} is: {}'.format(num_oranges,n,binoial_dist(n,num_oranges)))