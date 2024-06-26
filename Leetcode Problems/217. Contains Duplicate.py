'''217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False