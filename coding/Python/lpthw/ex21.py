# this is function tutorial

def add(a,b):
    print("adding {},{}:".format(a,b))
    return(a+b)

def subtract(a,b):
    print("subtract{},{}:".format(a,b))
    return(a-b)

def multiple(a,b):
    print("multiple {},{}".format(a,b))
    return(a*b)

def divide(a,b):
    print("divide {} ,{}:".format(a,b))
    return(a/b)

print("let's do some math with this function")

age=add(30,4)
weight=subtract(180,13)
height=multiple(33.5,2)
iq=divide(100,2)

print("age:{0},weight:{1},height:{2},iq:{3}".format(age,weight,height,iq))

print("lets do one puzzle")
what=add(age,multiple(weight,divide(height,subtract(iq,2))))
print("that's become:{0},can you do it by hand?".format(what))
