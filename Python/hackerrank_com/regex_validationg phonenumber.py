import re
n=int(input())

for i in range(n):
    s=input()
    if (s[0] in ['7','8','9']) and len(s)==10 and s.isdigit():
        print('YES')
    else:
        print('NO')

#other solution
if re.match(r'[789]\d{9}$',raw_input()):
    print 'YES'
else:
    print 'NO'
