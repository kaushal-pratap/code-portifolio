'''231. Power of Two

https://leetcode.com/problems/power-of-two/
'''
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 0:
            return False
        x = math.log(n,10)/math.log(2,10)
        if 2**int(x) == n:
            return True
        return False