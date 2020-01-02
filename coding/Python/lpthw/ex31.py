# this tutorial is related to nested if else
print("""You Enter e dark room with two doors
      Do you go through door #1 or door #2?""")

door=input(">")

if door =="1":
    print("there is a giant bear here eatnig a cheese cake.")
    print("What do you do?")
    print("1. take the cake")
    print("2 scratm at the bear.")

    bear=input(">")

    if bear =="1":
        print("the bear eats your face off.good job")
    elif bear =="2":
        print("the bear eats your legs off. Good job")

    else:
        print("Well ,doing {} is probably better.".format(bear))
        print("Bears runs away")

elif door =="2":
    print("you stare into the endless abyss ...")
    print("1. Blueberries")
    print("2. Yellow jacket")
    print("3 married with bear!")

    insanity=input(">")
    if insanity =="1" or insanity =="2":
        print("your body survived powered by a mind of jelly_beans")
        print("good job")
    else:
        print("the insanity kill you and you die")
        print("Good job")
else:
    print("your stumble around and fall on the knife and die anyway.")
