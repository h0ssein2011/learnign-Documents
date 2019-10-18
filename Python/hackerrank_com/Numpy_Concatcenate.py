import numpy

N,M,P = map(int ,input().split())
NP=numpy.array([input().strip().split() for i in range(N)],int)
MP=numpy.array([input().strip().split() for i in range(M)],int)

print(numpy.concatenate((NP,MP),axis=0))
