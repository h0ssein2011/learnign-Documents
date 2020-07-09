
import random
def Memory_Match(num_games=5):
    ls= random.sample(range(0,100), num_games)
    score=0
    
    for i in range(num_games):
        init=random.choice(ls)
        print(init)
        last_num=int(input('what was the last number? '))
        if last_num == init:
            score+=1
    print('your score is {} out of {}'.format(score,num_games)) 

Memory_Match(3)