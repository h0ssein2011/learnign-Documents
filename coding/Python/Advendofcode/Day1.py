
with open(file='day1.txt', mode='r') as f:
     nums = [int(line) for line in f]
     f.close()
increased = 0
print(nums[-5:]) # to check if the list is correct  
for i in range(0,len(nums)-1):
    if nums[i+1] > nums[i]:
        increased += 1
print(increased)


         
