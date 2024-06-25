'''977. Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/description/
'''
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        final_array = []
        for i in nums:
            final_array.append(i**2)
        return sorted(final_array)

