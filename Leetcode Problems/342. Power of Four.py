'''342. Power of Four

https://leetcode.com/problems/power-of-four/description/
'''
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 0:
            return False
        x = math.log(n)/math.log(4)
        tolerance = 1e-10
        return abs(x - round(x)) < tolerance