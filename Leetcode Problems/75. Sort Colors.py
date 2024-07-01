'''75. Sort Colors

https://leetcode.com/problems/sort-colors/description/
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        sum = 0
        for j in range(len(nums)-1):
            if nums[j] <= nums[j+1]:
                sum += 1
        if sum == len(nums)-1:
            return 


        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

        return self.sortColors(nums)