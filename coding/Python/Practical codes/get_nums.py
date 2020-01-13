nums=[]
with open('/media/hossein/0881-8560/sq_ml/got_errors2.txt','r') as f:

    contents = f.readlines()
    for line in contents:
        ind=line.find('index')
        num=line[ind+6:]
        nums.append(num)


    f.close()

with open('nums.txt','w') as f:
    f.write(','.join(nums) )
    f.close()