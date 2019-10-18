import numpy as np

coefs=[float(i) for i in input().split()]
x=float(input())
print(np.polyval(coefs,x))
