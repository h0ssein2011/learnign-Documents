# this is continuous of function variables

def cheese_and_crakcer(amount_cheese,amount_cracker):
    print("you have {0} and {1} cracker".format(amount_cheese,amount_cracker))
    print("man you have enough cheese for today!")
    print("take a blanket")

print("we can just give the function numbers directly")

cheese_and_crakcer(20,30)

print("or we can take from variables")

amount_cheese=20
amount_cracker=30

cheese_and_crakcer(amount_cheese,amount_cracker)
print("Or we can do math!")

cheese_and_crakcer(10+20,30+60)

print("and we can combine the two")

cheese_and_crakcer(amount_cheese+10 ,amount_cracker +30)
