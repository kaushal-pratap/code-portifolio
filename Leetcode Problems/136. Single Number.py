'''136. Single Number

https://leetcode.com/problems/single-number/
'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        HashMap = {}
        for i in nums:
            if i not in HashMap:
                HashMap[i] = 1
            else:
                HashMap[i] = HashMap[i] + 1
        for j in HashMap:
            if HashMap[j] == 1:
                return j