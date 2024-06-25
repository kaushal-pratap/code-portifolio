'''35. Search Insert Position

https://leetcode.com/problems/search-insert-position/
'''
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        HashMap = {}
        for i in range(len(nums)):
            HashMap[nums[i]] = i

        while len(nums) != 1:
            if target == nums[int(len(nums)/2)]:
                return HashMap[target]

            if target > nums[int(len(nums)/2)]:
                nums = nums[int(len(nums)/2):]

            else:
                nums = nums[:int(len(nums)/2)]
              
        if target > nums[0]:
            return HashMap[nums[0]] + 1
        return HashMap[nums[0]]