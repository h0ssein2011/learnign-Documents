with open(file='Day3.txt', mode='r') as f:
     nums = [int(line) for line in f]

     f.close()
# print(nums[:10]) # to check if the list is correct


num_str = ''
for i in range(12):
  
    slc = slice(i,i+1)
    pos = ''.join([str(p)[slc] for p in nums])
    if pos.count('1') > pos.count('0'):
        num_str += '1'
    elif pos.count('1') < pos.count('0'):
        num_str += '0'
    else:
        print('error')
print(num_str)
gamma_rate = num_str
epsilon_rate = num_str.replace('1','+').replace('0','1')
epsilon_rate = epsilon_rate.replace('+','0')

print(gamma_rate)
print(epsilon_rate)
gamma_rate_decimal = sum([pow(2,i) for i,p in enumerate(gamma_rate[::-1])])
epsilon_rate_decimal = sum([pow(2,i) for i,p in enumerate(epsilon_rate[::-1])])

print(gamma_rate_decimal)
print(epsilon_rate_decimal)
print(gamma_rate_decimal*epsilon_rate_decimal)
