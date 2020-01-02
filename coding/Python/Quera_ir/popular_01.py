# -*- coding: utf-8 -*-



import numpy as np

n = input("enter a num:")

n=str(n)
digits=[]
    
while sum(digits) < 9 :
    for i in range(len(n)):
        
        digits.append(int(n[i]))
    print(digits)

print(sum(digits))
    
    
    
    
        
