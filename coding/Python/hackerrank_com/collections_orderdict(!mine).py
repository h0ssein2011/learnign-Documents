# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ') #seprate a string to 3 part
    d[item] = d.get(item, 0) + int(quantity) #get velue an item if not exist 0
for item, quantity in d.items():
    print(item, quantity)
