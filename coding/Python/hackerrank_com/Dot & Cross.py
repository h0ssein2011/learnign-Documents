import numpy


n=int(input())
arr0=numpy.array([input().split() for _ in range(n) ],int)
arr1=numpy.array([input().split() for _ in range(n) ],int)


cross_prod=numpy.dot(arr0,arr1)

print(cross_prod)
