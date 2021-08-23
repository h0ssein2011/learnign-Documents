import random 
"""# in this game you get some shapes which is duplicated and
 you memorise the previous ones and based on that if you guess correctly wour score increase
 and the correct shape remove from the deck until all shapes finish
 https://kids.poki.com/game/sweety-memory"""

shapes = ['Gol','shokolat','girl','film','kelas']
shapes = shapes + shapes
random.shuffle(shapes)
print( shapes)
score = 100
cost = 0
for i in range(len(shapes)):
 
    cost += 1
    first = int(input('gues a location from 0 to {}'.format(len(shapes))))
    print('the first shape is: ',shapes[first])
    second = int(input('gues another location from 0 to {}'.format(len(shapes))))
    print('the second shape is: ',shapes[second])
    if shapes[first] == shapes[second] and shapes[first] != 'pooch' :
        score += 1
        print('Congrat you had a good guess and your score is: ',score)
        shapes = ['pooch' if x == shapes[first] else x for x in shapes]
        # shapes = list(filter(lambda a: a != shapes[first], shapes))
    elif shapes[second] == 'pooch' or shapes[first] != shapes[second]:
        score -= 1
        print('you selected this before or it is wrong! so your score will decrese to :',score)


print('your score is : ', score)
    



    






