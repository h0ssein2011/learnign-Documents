import numpy

n,m =map(int , input().split())
arr=numpy.array([input().split() for _ in range(n) ],int)
min_=numpy.min(arr,axis=1)
max_=numpy.max(min_ , axis=0)
print(max_)
