# this is list tutorial

ten_things="Apple Orange Crows Telephone Light Sugar"
print("Let's it seems that there arenot 10 things in the list let fix it")

stuff=ten_things.split(" ")
more_stuff=["hen", "egg", "tea", "mirror" ,"Boy","girl","sheep","Song"]

while len(stuff) != 10:
    next_one=more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)

    print("there is {} items now".format(len(stuff)))

print("there we go:",stuff)

print(stuff[1])
print(stuff[-1])# woaw fancy

print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
