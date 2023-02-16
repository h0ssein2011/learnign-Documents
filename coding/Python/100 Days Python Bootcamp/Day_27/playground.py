def add(*args):
    nums = [n for n in args]
    return sum(nums)

# print(add(5,7,8,87,51,41,48,98))


def calculate(n,**kwargs):
    # for k,v in kwargs.items():
    #     print(k,v)

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(7,add=3,multiply=5)