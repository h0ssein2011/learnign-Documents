# this is function tricks
def mode_5(x):
    return x % 5

def max_mode(x):
    print('which one is bigger:')
    print(max(x))

    print('which one has bigger mode by 5:' )
    print( max(x ,key=mode_5))
max_mode([108, 51, 14])
