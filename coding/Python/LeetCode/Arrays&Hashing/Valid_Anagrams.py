#https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, write a function to determine if t is an anagram of s.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

#Brute force solution
class Anagram(object):
    def __init__(self, s, t):
        hash_map_s = {c:s.count(c) for c in set(s)}
        hash_map_t = {c:t.count(c) for c in set(t)}
        return hash_map_s == hash_map_t

# Better solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_dict_s = {c:s.count(c) for c in set(s)}
        hash_dict_t = {c:t.count(c) for c in set(t)}
        
        for c in hash_dict_s:
            if hash_dict_s[c] != hash_dict_t.get(c,0):
                return False 
        return True

# better s which has less complexity than the above solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
