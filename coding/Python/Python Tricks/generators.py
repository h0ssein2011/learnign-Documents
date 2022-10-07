""" 
Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory,

"""
def generator_func(n):
    for i in range(n):
        yield i

for i in generator_func(10):
    print(i)

gen = generator_func(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) 


