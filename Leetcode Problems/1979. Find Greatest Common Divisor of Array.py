'''1979. Find Greatest Common Divisor of Array

https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
'''

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        small = min(nums)
        big = max(nums)
        divisor = 0
        for i in range(1,big+1):
            if small % i == 0 and big % i == 0:
                divisor = i
        return divisor