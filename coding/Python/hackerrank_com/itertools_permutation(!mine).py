# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
