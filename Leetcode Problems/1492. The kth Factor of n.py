'''1492. The kth Factor of n

https://leetcode.com/problems/the-kth-factor-of-n/description/
'''


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1,int(n/2)+1):
            if n % i == 0:
                factors.append(i)
        factors.append(n)

        if k > len(factors):
            return -1
        return int(factors[k-1])