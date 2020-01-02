import numpy

arr=list(map(int , input().split()))
arr=numpy.array(arr)
print(numpy.reshape(arr,(3,3)))
