#unpack a list
my_list=['asm',1,3,5,7,(2019,8,7)]

txt,number,date=my_list[0],my_list[1:-1],my_list[-1]



print(txt)
print(number)
print(date)


#unpack a huge list
import numpy as np
ls=[i for i in range(100)]
print(ls)


def get_middle(x):
    first,*middle,last=x
    print(middle )

get_middle(ls)
