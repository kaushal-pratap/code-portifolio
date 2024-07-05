'''34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
'''

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
                break
        j = len(nums) -1
        while j >= 0:
            if nums[j] == target:
                result.append(j)
                break
            j -= 1

        if nums[i] != target:
            return [-1,-1]
        return [i,j]