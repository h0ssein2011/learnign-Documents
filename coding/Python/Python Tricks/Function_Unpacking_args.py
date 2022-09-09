def vec_reader(x,y,z):
    return f'<{x},{y},{z}>'

print('Enter data manually')
print(vec_reader(4,5,3))

print('Enter data with address from a list or tupple')
vec = [4,5,3]
print(vec_reader(vec[0],vec[1],vec[2]))

print('Enter data with unpacking')

print(vec_reader(*vec))

# use a dictionary and unpack it
vec_dict = {'x':1,'y':2,'z':3}

print('unpack values a dictionary')
print(vec_reader(**vec_dict))

print('unpack keys a dictionary')
print(vec_reader(*vec_dict))
