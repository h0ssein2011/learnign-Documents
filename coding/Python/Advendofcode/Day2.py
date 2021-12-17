with open(file='Day2.txt', mode='r') as f:
    structure = [line for line in f.read().splitlines()[:] ]
    guides = [line.split()[0] for line in structure]
    nums = [int(line.split()[1]) for line in structure] 
    f.close()
# test that file reads correctly    
# print(guides[:])
# print(nums[:])

horizintal = 0
vertical = 0

i = 0
for g in guides:
    if g == 'forward':
        horizintal += nums[i] 
    elif g == 'down':
        vertical += nums[i]
    elif g == 'up':
        vertical -= nums[i]
    else:
        print('error')
    i += 1
print("Part 1's solution is: ",horizintal* vertical)


i=0
horizintal = 0
vertical = 0
aim = 0
for g in guides:
    if g == 'forward':
        horizintal += nums[i]
        vertical += nums[i] * aim

    elif g == 'down':
        aim += nums[i]
    elif g == 'up':
        aim -= nums[i]
    else:
        print('error')
    i += 1
print('horizintal', horizintal)
print('vertical', vertical)
print('aim', aim)

print("Part 2's solution is: ", horizintal* vertical)
