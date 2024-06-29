'''2427. Number of Common Factors

https://leetcode.com/problems/number-of-common-factors/
'''
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        if a > b:
            for i in range(1,b+1):
                if a % i == 0 and b % i == 0:
                    count += 1
        else:
            for j in range(1, a+1):
                if a % j == 0 and b % j == 0:
                    count += 1
        return count