# find a isPalindrome function
#https://leetcode.com/problems/valid-palindrome/
# Bruteforce approach 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower().replace(' ','')
        s1 = ''.join(ch for ch in s1 if ch.isalnum())
        s2=s1[::-1]
        return s1 == s2

# Low level approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1

        while l < r:
            while l < r and not self.alphnum(s[l]):
                l += 1
            while l < r and not self.alphnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
        return True



    def alphnum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') 
        or 
        ord('a') <= ord(c) <= ord('z') 
        or 
        ord('0') <= ord(c) <= ord('9'))