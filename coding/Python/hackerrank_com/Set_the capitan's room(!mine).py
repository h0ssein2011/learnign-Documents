from collections import defaultdict

k = int(input())
rooms = input().strip().split()

ct = defaultdict(int)

for i in rooms:
    ct[i] += 1

print([i for i in ct if ct[i] == 1][0])
