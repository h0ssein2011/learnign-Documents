with open(file='Day3.txt', mode='r') as f:
     nums = [line for line in f]

     f.close()
# print(nums[:10]) # to check if the list is correct

gamma_rate =[]
epsion_rate = []
for i in range(12):
    num_list = [p[i] for p in nums]
    if num_list.count('1') > num_list.count('0') :
        gamma_rate.append(1)
        epsion_rate.append(0)

    else:
        gamma_rate.append(0)
        epsion_rate.append(1)
    print( i , num_list.count('1') , num_list.count('0') , gamma_rate[i])

print(gamma_rate)
print(epsion_rate)
gamma_rate_decimal = sum([int(p)*pow(2,i) for i,p in enumerate(gamma_rate[::-1])])
epsion_rate_decimal = sum([int(p)*pow(2,i) for i,p in enumerate(epsion_rate[::-1])])

print(gamma_rate_decimal)
print(epsion_rate_decimal)
print(gamma_rate_decimal*epsion_rate_decimal)
  

