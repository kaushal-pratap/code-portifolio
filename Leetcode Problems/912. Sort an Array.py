'''912. Sort an Array

https://leetcode.com/problems/sort-an-array/description/
'''

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.Merge(left_half, right_half)

    def Merge(self,left_half,right_half):
        i = j = 0
        result = []
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1

        result.extend(left_half[i:])
        result.extend(right_half[j:])
        return result