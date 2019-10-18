n_test=int(input())
for _ in range(n_test):
    n_A=int(input())
    A=list(map(int ,input().split()))


    n_B=int(input())
    B=list(map(int ,input().split()))

    if sum([1 for i in A if i in B]) == n_A :

        print(True)
    else:
        print(False)
