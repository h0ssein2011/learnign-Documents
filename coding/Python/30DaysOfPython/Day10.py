for i in range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i+=1

for i in range(7):
    print('#'*i)

for i in range(8):
    print('# # # # # # # #')

for i in range(11):
    print(f'{i} x {i} = {i *i}')

pgs = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for pg in pgs:
    print(pg)

for i in range(101):
    if i % 2 == 0 :
        print(i)


for i in range(101):
    if i % 2 != 0 :
        print(i)

sum = 0
for i in range(101):
    sum +=i
print(sum)


sum_odd = 0
sum_even = 0

for i in range(101):
    if i % 2 == 0 :
        sum_even += i
    else :
        sum_odd += i
print(f'sum even is {sum_even}')
print(f'sum odd is {sum_odd}')


import urllib.request  # the lib that handles the url stuff


url = 'https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py'
for line in urllib.request.urlopen(url):
    print(line)

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruits = []

for fru in fruits[::-1]:
    new_fruits.append(fru)
print(new_fruits)



import pandas as pd
