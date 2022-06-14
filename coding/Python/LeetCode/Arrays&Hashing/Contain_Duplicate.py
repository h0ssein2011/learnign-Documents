""" https://leetcode.com/problems/contains-duplicate/
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Example 1:
Input: [1,2,3,1]
Output: true
Example 2:
Input: [1,2,3,4]
Output: false
Example 3:
Input: [1,1,1,3,3,4,3,4]
Output: true
 """
 #brute force solution
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
# check if there is a duplicate in the list
assert Solution().containsDuplicate([1,2,3,1]) == True
assert Solution().containsDuplicate([1,2,3,4]) == False
assert Solution().containsDuplicate([1,1,1,3,3,4,3,4]) == True

# Hashing Solution
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Hashset = set()
        for num in nums:
            if num in Hashset:
                return True
            Hashset.add(num)
        return False
# check if there is a duplicate in the list
assert Solution().containsDuplicate([1,2,3,1]) == True
assert Solution().containsDuplicate([1,2,3,4]) == False
assert Solution().containsDuplicate([1,1,1,3,3,4,3,4]) == True

