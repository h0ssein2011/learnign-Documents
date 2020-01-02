# this is while loop tutorial

i=0
numbers=[]

while i < 6:
    print("at the top of i is:{}".format(i))
    numbers.append(i)

    i+=1
    print("the number now:",numbers)
    print("at the bottmon of i {}".format(i))

print("the numbers:")
for num in numbers:
    print(num)


# study drill

def create_list(num):
    numbers=[]
    for i in range(num):
        numbers.append(i)
    print("the numbers is:",numbers)

create_list(6)
