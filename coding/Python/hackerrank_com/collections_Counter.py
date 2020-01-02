# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n_shoes=int(input())
size_available=Counter(map(int , input().split()))
n_customer=int(input())

purchase=0
for i in range(n_customer):
    size_cust,price=map(int , input().split())
    if size_available[size_cust]:
        purchase += price
        size_available[size_cust] -= 1

print(purchase)
