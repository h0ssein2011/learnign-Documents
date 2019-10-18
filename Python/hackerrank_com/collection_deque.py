# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N=int(input())
d=deque()
for i in range(N):
    eval('d.{0}({1})'.format(*input().split()+['']))

for i in d:
    print(i,end=' ');
