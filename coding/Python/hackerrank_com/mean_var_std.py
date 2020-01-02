from numpy import set_printoptions, array, mean, var, std
set_printoptions(legacy='1.13')

N, M = map(int, input().split())

arr = array([list(map(int, input().split())) for _ in range(N)])

print(mean(arr, axis=1))
print(var(arr, axis=0))
print(std(arr, axis=None))
