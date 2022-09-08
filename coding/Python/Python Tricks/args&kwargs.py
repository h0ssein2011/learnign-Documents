
def yell(title,*args):
    print(title)
    for arg in args:
        print(arg)

def yell2(title,**kwargs):
    print(title)
    for tit,text in kwargs.items():
        print(tit,'-->',text)

yell('Test args',"I can do it."
        ,"world is not a good place but worth to fight."
        ,"That is all I could do for today.")


yell2('Test kwargs',blog_1 = "I can do it."
                    ,blog_2 = "world is not a good place but worth to fight."
                    ,blog_3 = "That is all I could do for today.")
