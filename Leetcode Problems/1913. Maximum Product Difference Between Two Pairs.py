'''1913. Maximum Product Difference Between Two Pairs

https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
'''

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[len(nums)-1]*nums[len(nums)-2] - nums[0]*nums[1])