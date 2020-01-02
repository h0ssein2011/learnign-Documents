# for loop tutorial
the_count=[1,2,3,4]
fruits=['apples','orange','pears','apricots']
change=[1,'pennies',2,'dims',3,'quarters']

# this is just go trough the list
for number in the_count:
    print("this is count:{}".format(number))

#same as above
for fruit in fruits:
    print("fruit of type:{}".format(fruit))
# also we can go through mixed list
#notice we have to put{} to see wahts going on
for i in change:
    print("I got {}".format(i))

# we can also build lists first stat with an empty lists
elements=[]
# then use a range function to do 0 to 5 count:
for i in range(0,6):
    print("adding {}".format(i))
    #append is a fucntion that list undrestand
    elements.append(i)

#now we can print them out too:
for i in elements:
    print("Element was{}".format(i))
