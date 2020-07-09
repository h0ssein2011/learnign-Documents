
def Poki_game(l):
    played =[]
    num_shots = len(l)-1
    for i in range(num_shots):
        shot = int(input('select a Poki'))
        if shot in played or shot not in l:
            print('You lost!....')
            break
        else:
            played.append(shot)

    if len(played)+1 == len(l):
        print('you won')

Poki_game([1,5,6,8,9])
