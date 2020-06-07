

#https://www.hackerrank.com/challenges/between-two-sets/problem
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

def getTotalX(a, b):
    # Write your code here
    # max_a = max(a)
    # min_b = min(b)

    # nums=[]
    # for i in range(1,int(min_b / max_a)+1):
    #     if min_b % i * max_a == 0:
    #         nums.append(i * max_a)
    # return sum([1 for x,y in zip(nums,b) if y % x ==0 ])

    ausgabe = 0
    for q in range(max(a), min(b) +1):
        if all(q % arr == 0 for arr in a) and all(brr % q == 0 for brr in b):
            ausgabe += 1
    
    return(ausgabe)

total = getTotalX(arr, brr)



#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/
n = int(input())

scores = [int(input().rstrip().split()[0]) for i in range(n)]


def breakingRecords(scores):
    num_max = 0
    num_min = 0

    for i in range(len(scores)-1):
        if scores[i+1] > max(scores[0:i+1]):
            num_max +=1
        if scores[i+1] < min(scores[0:i+1]):
            num_min +=1
    return (num_max , num_min)
result = breakingRecords(scores)
print(result)


#https://www.hackerrank.com/challenges/the-birthday-bar/problem

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])


def birthday(s, d, m):
    # nums =0
    # for i in range(len(s)):
    #     if sum(s[i:i+m]) == d:
    #         nums+=1
    nums=sum([1 for i in range(len(s)) if sum(s[i:i+m]) == d ])
    return(nums)

result = birthday(s, d, m)



## https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))


def divisibleSumPairs(n, k, ar):
    # counts=0
    # ln=len(ar)
    # for i in range(ln):
    #     for j in range(1,ln):
    #         if i < j and (ar[i]+ar[j]) % k == 0:
    #             counts +=1
    counts= sum([1 for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j]) % k == 0] )

    return counts

result = divisibleSumPairs(n, k, ar)



## https://www.hackerrank.com/challenges/migratory-birds/problem

arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

def migratoryBirds(arr):
    d={}
    for i in set(arr):
        d[i] = arr.count(i)

    maxval = max(d.values())
    res = [k for k, v in d.items() if v==maxval][0]
    return res

result = migratoryBirds(arr)



#https://www.hackerrank.com/challenges/day-of-the-programmer/problem
year = int(input().strip())

def dayOfProgrammer(year):
    if (year == 1918):
        return '26.09.1918'

    elif ((year <= 1917) and (year%4 == 0)) or 
                ((year > 1918) & (year%400 == 0 or
                ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return('13.09.{}'.format(str(year)))


result = dayOfProgrammer(year)



ar=[10 ,20, 20, 10 ,10 ,30 ,50 ,10 ,20]
print(sum([int(ar.count(i)/2) for i in set(ar)]))

print(ar.count())

print(100 // 8)
print(100 % 8)


























select right_table.country , usr_ages.Age_group
        -- ,sum(case when (cast(nf.created_date as date) - cast ( tr.created_date  as date)) between 0 and 7  then 1 else 0 end) / count(distinct nf.user_id) as AVG_transactions_before_pn
        -- ,sum(case when ( cast(tr.created_date  as date) -cast (nf.created_date as date)) between 0 and 7  then 1 else 0 end)/ count(distinct nf.user_id) as AVG_transactions_after_pn
from 
(
 select users.user_id,
case 
    when (2020 - birth_year) between 19 and 30 then 'age_19_30_yrs'
	when (2020 - birth_year) between 31 and 40 then 'age_31_40_yrs'
	when (2020 - birth_year) > 40 then 'greater_than_40_yrs' 
	else 'Other' END as Age_group
from users ) as usr_ages
right Join 
( 
(select created_date,status,user_id
from notifications
-- filter on the users who recieved the notification alert
where status = 'SENT' ) as nf
 left join transactions as tr
 on nf.user_id = tr.user_id  
 left join users as usr 
 on tr.user_id = usr.user_id ) as right_table
 on usr_ages.user_id = right_table.user_id
 
-- group by  usr.country,Age_group

