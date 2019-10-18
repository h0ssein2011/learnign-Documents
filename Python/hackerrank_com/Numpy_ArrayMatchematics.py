import numpy

N,M=map(int , input().split())
A=numpy.array([input().strip().split() for i in range(N)],dtype=int)
B=numpy.array([input().strip().split() for i in range(N)],dtype=int)


print(A+B , A-B,A*B , A//B,A%B,A**B ,sep='\n')
