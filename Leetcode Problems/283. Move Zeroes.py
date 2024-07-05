'''283. Move Zeroes

https://leetcode.com/problems/move-zeroes/description/
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        count = 0
        result = []
        for i in nums:
            if i != 0:
                result.append(i)
            else:
                count += 1
        while count >0:
            result.append(0)
            count -= 1
        for j in range(len(nums)):
            nums[j] = result[j]
