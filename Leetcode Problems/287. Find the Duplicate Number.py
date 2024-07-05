'''287. Find the Duplicate Number

https://leetcode.com/problems/find-the-duplicate-number/description/
'''

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        HashMap = {}
        for i in nums:
            if i in HashMap:
                return i
            HashMap[i] = 0