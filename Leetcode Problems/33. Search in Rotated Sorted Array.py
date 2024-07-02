'''33. Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left < right:
            pivot = (left + right)//2
            if nums[pivot] > nums[right]:
                left = pivot + 1
            else:
                right = pivot 
        pivot = left

        if target >= nums[pivot] and target <= nums[len(nums)-1]:
            left2 = pivot
            right2 = len(nums)-1
        else:
            left2 = 0
            right2 = pivot -1 

        while left2 <= right2:
            middle = (left2 + right2)//2
            if target == nums[middle]:
                return middle 
            elif target > nums[middle]:
                left2 = middle + 1
            else:
                right2 = middle - 1
        
        return -1 