# how to use decorators


def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def greet():
    return 'Hello!'

greet()


# use two decorators on a function 
def H1(func):
    def wrapper():
        return "<h1>" + func() + "</h1"
    return wrapper

def emphsise(func):
    def wrapper():
        return "<em>" + func() + "</em"
    return wrapper

@H1
@emphsise
def greet():
    return 'Hello!'

greet()