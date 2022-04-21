def binary_search(data,answer):
    data = sorted(data)
    low = 0
    high = len(data)-1
    found = False
    count = 0
    while found == False:
        count += 1
        guess = int(input())
        if guess == answer:
            print(f'Great you win! in {count} iteration')
            found = True
        if guess < answer:
            print('Your guess is too low lets have another guess')
            low = guess +1
        else :
            print('Your guess is too high lets have another guess')
            high = guess - 1
binary_search(data=range(100),answer=56)

