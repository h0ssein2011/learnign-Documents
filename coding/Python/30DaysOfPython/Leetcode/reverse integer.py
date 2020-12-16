class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0)-(x < 0)
        r = int(str(x*s)[::-1])

        if s*r <= -2 ** 31 - 1 or s*r >= 2 ** 31 - 1:
            return 0
        return s*r


def isPalindrome(x: int):
    res = False
    if x <= 0:
        pass

    else:
        count = 0
        X = x
        while (X > 0):
            X = X//10
            count += 1
        print(x)
        half = 1+count//2
        print('digits:', half)
        x = str(x)
        left = x[:half]
        print('left', left)
        right = x[half-1::]
        print('right', right)
        if left == right:
            res = True
    return res


isPalindrome(121)
