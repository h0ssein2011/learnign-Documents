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
portfoilo=[{'name':'IBM','share':100,'price':200},
           {'name':'Tesla','share':80,'price':150},
           {'name':'Apple','share':90,'price':220},
           {'name':'MS','share':60,'price':120},
           {'name':'Google','share':98,'price':240},
           {'name':'IIG','share':'20','price':10}
           ]
cheap=heapq.nsmallest(3,portfoilo,key=lambda s:s['price'])
expensive=heapq.nlargest(3,portfoilo,key=lambda s:s['price'])
print(cheap)
print(expensive)

nums_sorted=sorted(nums)
nums_heap=heapq.heapify(nums)


#multidict(dicnaries with mulitply valus)

dits={'a':[1,4,8],'b':[1,7]}
dicts

#another option is defaultdict from collections
from collections import defaultdict

#2 type use list and use set
d=defaultdict(list)
d['a'].append(1)
d['a'].append(3)
d['b'].append(5)
d['b'].append(7)
d

d=defaultdict(set)
d['a'].add(7)
d['a'].add(6)
d['a'].add(5)
d['b'].add(3)
d['b'].add(4)
d

# keep dictionaries in order
from collections import OrderedDict

d=OrderedDict()

d['foo']=1
d['bar']=3
d['jerk']=2

d

for key in d.keys():
    print(key,d[key])


# calculation with dictionaries
prices={'Apple':23.6,
        'IBM':33.4,
        'IIG':14.1,
        'FB':7.9
}

min_price=min(zip(prices.values(),prices.keys()))
max_price=max(zip(prices.values(),prices.keys()))

min_price,max_price


#commonility in two dictionaries
a={'x':1,'y':2,'z':3 }
b={'w':10,'x':11,'y':2}

a.keys() - b.keys()

a.keys() & b.keys()
a.values() & b.values()

a.items() &  b.items()
a.items() -  b.items()

#remove certain keys
c={key:a[key] for key in a.keys() -{'z','w'}}
c

# remove duplicate and remain order

def dedupe(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a=[1,52,1,9,1,5,10]
list(dedupe(a))


#naming a slice

record = '....................100        513.25  ..........'
cost=int(record[20:31]) * float(record[31:38])
cost

#2nd approach
share=slice(20,32)
price=slice(31,38)

cost=int(record[slice]) * float(record[price])
cost


#find most common in a sequence
words=['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under']

from collections import Counter

word_count=Counter(words)
top3=word_count.most_common(3)
top3

morewords = ['why','are','you','not','looking','in','my','eyes']

#add manually to word_count
for word in morewords:
    word_count[word] +=1
word_count

#another approach
word_count.update(morewords)
word_count

#combine two
a=Counter(words)
b=Counter(morewords)

c=a+b
d=a-b
c,d


#sort dictionairs

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname=sorted(rows, key=itemgetter('fname'))


rows_by_uid=sorted(rows, key=itemgetter('uid'))
rows_by_uid

#another approach by lambda
rows_by_fname=sorted(rows, key=lambda r:r['fname'])




#group items based on a field
from operator import itemgetter
from itertools import groupby

rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

#first sorted


rows.sort(key=itemgetter('date'))

for date , items in groupby(rows ,key=itemgetter('date')):
    print(date)

    for i in items :
        print(' ',i)


#fliltering in a list
#list comprehention
my_vals=[7,8,-2,9,-8,7,-2,-44,42,89]
pos_list=[n for n in my_vals if n >0]
pos_list
type(pos_list)

#generator
pos_gens=(n for n in my_vals if n >0)
pos_gens
type(pos_gens)



#use filter
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False

int_values=list(filter(is_int , values))
int_values

my_solo=[n for n in values if is_int(n)]
my_solo

#select from two list
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5=[n>5 for n in counts]
more5

list(compress(addresses, more5))
