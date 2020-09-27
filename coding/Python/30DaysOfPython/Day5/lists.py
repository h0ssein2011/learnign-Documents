empty_lst = []
sports = ['football','vollybal','swimming','hockey','runing']
print(len(sports))

print('first_item:',sports[0])
print('mid_item:',sports[int(len(sports)/2)])
print('last_item:',sports[-1])


mixed_data_types = ['Hossein','Mortazavi',1.67,'Tehran']
it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(mixed_data_types)
print(it_companies)
print('number of companies:' , len(it_companies))
print('First company:',it_companies[0])
print('mid company:',it_companies[int(len(it_companies) / 2)])
print('Last company:',it_companies[-1])
print(it_companies)
it_companies.append('Paroo')
print(it_companies)

it_companies.insert(int(len(it_companies)/2),'my_baby')
print(it_companies)

it_companies[3]=it_companies[3].upper()
print(it_companies)

# it_companies = ['#'+ comp for comp in it_companies]
print(it_companies)

print('#Paroo' in it_companies)


it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True) 
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies[int(len(it_companies)/2)])

it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']

it_companies.pop(0)
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
Full_stack= front_end
print(Full_stack)

Full_stack.append(('SQL'))
print(Full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 35 , 42,78, 24,44 ,3,1,11,124,245,4]
ages.sort()
print('min is:', min(ages))
print('max is:', max(ages))

ages.append(min(ages))
ages.append(max(ages))
ages.sort()


print(ages)
print(len(ages))

if len(ages ) % 2 ==0 :
    print('median is:' , sum( ages[int(len(ages)/2)-1 :int(len(ages)/2)+1])/2)
else:
    print('median is:' , ages[int(len(ages)/2)])

avg = sum(ages)/ len(ages)
print(avg)

print(min(ages) , max(ages))
print(avg - min(ages) == avg - max(ages) )

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, USA,*rest = countries
print(rest)











