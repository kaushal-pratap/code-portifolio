'''268. Missing Number

https://leetcode.com/problems/missing-number/description/
'''
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        HashMap = {}
        j = 0
        counter = 0
        for i in nums:
            HashMap[i] = j
            j += 1
        
        while True:
            if counter not in HashMap:
                return counter
            counter += 1