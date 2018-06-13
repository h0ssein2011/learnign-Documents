#unpacking
p=(4,5)
a,b=p



print(a,b)

data=['ACME',50,90.1,(2012,11,12)]

name,shares,price,date=data

print(name,shares,price,date)


s='Hello'

a,b,c,d,e=s

print(a +'\n',b +'\n',c +'\n',d +'\n',e+ '\n')


# probelm 2:unpacking with *
from numpy import mean
def drop_first_last(grades):
    first,*middle,last = grades
    return middle,mean(middle)

grades=[1,4,5,1,8,9,12,36,89]
drop_first_last(grades)

#compare avgs
sales_record=[5,6,25,12,14,6,7]
*pre_quarters,curr_quarter=sales_record
avg_previous=sum(pre_quarters)/len(pre_quarters)
print(avg_previous,'//',curr_quarter)

#unpacking on tupels
records=[('foo',1,2),('bar',3),('foo',4,5)]

def do_foo(x,y):
    print(x,y)

def do_bar(x):
    print(x)



for tag,*args in records:
    if tag == 'food':
        do_foo(args)
    else:
        do_bar(args)


#use _ to ignore things
data=['ACME',50,90.1,(2012,11,12)]

name,*_,(*_,year)=data
name,year
