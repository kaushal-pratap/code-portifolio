'''2535. Difference Between Element Sum and Digit Sum of an Array

https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
'''

class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for i in nums:
            for j in str(i):
                digit_sum += int(j)
            element_sum += i
        return abs(element_sum - digit_sum)