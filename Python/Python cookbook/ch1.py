p=(4,5)
a,b=p



print(a,b)

data=['ACME',50,90.1,(2012,11,12)]

name,shares,price,date=data

print(name,shares,price,date)


s='Hello'

a,b,c,d,e=s

print(a +'\n',b +'\n',c +'\n',d +'\n',e+ '\n')


# probelm 2:unpacking
from numpy import mean
def drop_first_last(grades):
    first,*middle,last = grades
    return middle,mean(middle)

grades=[1,4,5,1,8,9,12,36,89]
drop_first_last(grades)
