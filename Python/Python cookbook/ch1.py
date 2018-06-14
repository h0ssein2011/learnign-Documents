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


#keep last items in a list

from collections import deque

def search(lines,pattern ,history=5):
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

#example use a file
#if __name__== __main__:
with open('samplefile.txt') as f:
     for line ,prevlines in search(f,'python',5):

         for pline in prelines:
             print(pline,end='')
         print(line,end='')
         print('-'*20)

#deque application
q=deque(max maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)


#finding largest and smallest in a list
import heapq

nums=[-10,20,15,17,11,57,16,74,3]
largest=heapq.nlargest(3,nums)
lowest=heapq.n(3,nums)
print(largest,lowest)

#also in a list or collections
