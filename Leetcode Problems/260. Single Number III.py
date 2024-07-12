'''260. Single Number III

https://leetcode.com/problems/single-number-iii/description/
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        HashMap = {}
        result = []
        for i in nums:
            if i in HashMap:
                HashMap[i] += 1
            else:
                HashMap[i] = 1
        for j in HashMap:
            if HashMap[j] == 1:
                result.append(j)
        return result