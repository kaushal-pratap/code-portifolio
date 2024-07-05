'''704. Binary Search

https://leetcode.com/problems/binary-search/description/
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                right = middle -1 
                
            else:
                left = middle + 1
        return -1