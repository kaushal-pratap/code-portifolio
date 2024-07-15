'''1822. Sign of the Product of an Array

https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
'''

class Solution:
    def signFunc(self,x):
        if x > 0:
            return 1
        if x < 0:
            return -1
        else:
            return 0
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for i in nums:
            product = product*i
        return self.signFunc(product)