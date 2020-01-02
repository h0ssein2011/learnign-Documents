# my answer
def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    combs=[s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    Stuart_combs=[]
    kevin_combs=[]

    for sub in combs:
        if sub[0] in vowels:
            kevin_combs.append(sub)
        else:
            Stuart_combs.append(sub)

    if len(Stuart_combs) > len(kevin_combs):
        print('Stuart',len(Stuart_combs),sep=' ')
    else:
        print('Kevin' ,len(kevin_combs) , sep=' ')

if __name__ == '__main__':
    s = input()
    minion_game(s)


#the correct None
def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    kevsc = 0
    stusc = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
