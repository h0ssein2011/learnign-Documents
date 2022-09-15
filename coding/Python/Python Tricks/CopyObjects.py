#Shallow copy

x = [[1,2,3],[4,5,6]]
y = list(x) 
z = x


x[0] = 78
print(f'x is: {x}')
print(f'y is: {y}')
print(f'z is: {z}')

print('*'*100)
# deep copy 
import copy 
x = [[1,2,3],[4,5,6]]
p = copy.deepcopy(x)
x[0] = 78

print(f'x is: {x}')
print(f'y is: {y}')
print(f'p is: {p}')
