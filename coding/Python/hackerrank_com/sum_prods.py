import numpy
n,m=map(int, input().split())
arr=numpy.array([input().split() for _ in range(n)],int)

sums=numpy.sum(arr,axis=0)
prods=numpy.prod(sums,axis=0)
print(prods)
