'''172. Factorial Trailing Zeroes

https://leetcode.com/problems/factorial-trailing-zeroes/description/
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n = n//5
            count += n
        return count