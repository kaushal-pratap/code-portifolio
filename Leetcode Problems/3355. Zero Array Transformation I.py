'''3355. Zero Array Transformation I

https://leetcode.com/problems/zero-array-transformation-i/description/
'''
class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        diff = [0]*(len(nums)+1)
        for left,right in queries:
            diff[left] += 1
            diff[right+1] -= 1
        for i in range(1,len(diff)):
            diff[i] += diff[i-1]
        for i in range(len(nums)):
            if nums[i] - diff[i] > 0:
                return False
        return True