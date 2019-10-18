import re
N=int(input())

for i in range(N):
    ans=True
    s=input()
    try:
        re.compile(s)
    except re.error:
        ans=False
    print(ans)
