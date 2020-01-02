N=int(input())
A=set(map(int , input().strip().split()))
M=int(input())
B=set(map(int , input().strip().split()))

difs=sorted(list(A.difference(B))+list(B.difference(A)))

[print(i) for i in difs]
