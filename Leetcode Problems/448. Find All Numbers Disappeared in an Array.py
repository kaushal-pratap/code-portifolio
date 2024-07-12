'''448. Find All Numbers Disappeared in an Array

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
'''
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        HashMap = {}
        for i in nums:
            HashMap[i] = i
        for j in range(1,n+1):
            if j not in HashMap:
                result.append(j)

        return result