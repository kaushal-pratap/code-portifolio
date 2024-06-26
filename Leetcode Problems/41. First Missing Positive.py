'''41. First Missing Positive

https://leetcode.com/problems/first-missing-positive/
'''
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        HashMap = {}
        for i in nums:
            HashMap[i] = i
        j = 1
        while True:
            try:
                if HashMap[j] == j:
                    j += 1
            except:
                return j