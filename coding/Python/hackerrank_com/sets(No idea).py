n,m = map(int , input().split())
l=[int(i) for i in input().split()]
A=set(int(i) for i in input().split())
B=set(int(i) for i in input().split())

happyness=sum([1 if i in A else -1  if i in B else 0 for i in l])


print(happyness)
