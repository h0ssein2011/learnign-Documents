import numpy

N, M = map(int, input().split())
arr=numpy.array([input().strip().split() for i in range(N)],int)
print(numpy.transpose(arr))
print(arr.flatten())
