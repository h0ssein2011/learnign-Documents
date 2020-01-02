# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A=list(map(int , input().split()))
B=list(map(int , input().split()))
prods_list=list(product(A,B))
for i in prods_list:
    print(i, end =" ")
