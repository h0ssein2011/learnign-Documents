#this is life game it means that you give me some basic info about urself I will give you what you do know

#cool
gender=input("are you man or woman:")
age=input("how old are you?")

if age <=10:
    print("you are so young be happy with your family!")

elif age >10 and age <=20:
    print("this is the best time to you learn basic life rules")

elif age >20 and age <=35:
    if gender =="man":
        print("try find a job to learn new things")

    elif gender=="woman":
        print("try learn to find a husband!")

    else:
        gay("sorry")

elif age >35 and age <=50:
    if gender =="man":
        print("try to make a family and raise them")

    elif gender=="woman":
        print("try riase your family")

    else:
        gay("sorry")

else:
    print("thats a time that you be happy with your kids and your family")


def gay(do_this):
    print("it seems that you are a gay",do_this)
