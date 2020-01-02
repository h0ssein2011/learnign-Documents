n,m=map(int , input().split())

def gradiants(n,m):
    if n > 0 and m >0:
        output = 1
    elif n < 0 and m > 0:
        output =2
    elif n < 0 and m < 0:
        output = 3
    else:
        output =4

    print(output)
gradiants(n,m)


