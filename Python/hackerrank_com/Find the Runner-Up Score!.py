if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr=sorted(set(arr))
runner_up=arr[-2]
print(runner_up)


# editorial solution
