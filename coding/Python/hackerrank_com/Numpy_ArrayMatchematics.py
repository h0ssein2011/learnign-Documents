import numpy

N,M=map(int , input().split())
A=numpy.array([input().strip().split() for i in range(N)],dtype=int)
B=numpy.array([input().strip().split() for i in range(N)],dtype=int)


print(A+B , A-B,A*B , A//B,A%B,A**B ,sep='\n')


from itertools import combinations

a = [1,2,3]

combinations(a)


from itertools import combinations
def find_pairs_with_given_difference(arr, k):

    
    ls=[]
    
    print(list(combinations(arr,2)))
print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
    