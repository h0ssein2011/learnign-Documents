import  numpy as np

list_nums=np.random.randint(3, 100 ,30000)
# print(list_nums)

mean_population = np.mean(list_nums)
var_population= np.sum(np.square(list_nums - mean_population)) / (len(list_nums))

#check the calculation
if var_population == np.var(list_nums):
    print('the calculation is ok')
else:
    print('there is something wring with the calculation{},{}'.format(var_population ,np.var(list_nums)))

var_sample = np.sum(np.square(list_nums - mean_population)) / (len(list_nums)-1)
print('variance sample is: ',var_sample)
if var_sample == np.var(list_nums ,ddof=1):
    print('the calculation is ok')
else:
    print('there is something wring with the calculation{},{}'.format(var_population ,np.var(list_nums)))

#calculate std
print('std population is:',np.sqrt(var_population))
print('std sample is:',np.sqrt(var_sample))


#as the population data increase the estimate of population will improve