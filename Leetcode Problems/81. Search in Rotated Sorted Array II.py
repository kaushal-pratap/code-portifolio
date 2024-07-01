'''81. Search in Rotated Sorted Array II

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
'''

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        new = nums
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums = nums[i+1:] + new[:i+1]
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return True
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return False