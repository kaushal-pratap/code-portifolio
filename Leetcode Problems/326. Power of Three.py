'''326. Power of Three

https://leetcode.com/problems/power-of-three/
'''
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 0:
            return False
        x = math.log(n)/math.log(3)
        tolerance = 1e-10
        return abs(x - round(x)) < tolerance