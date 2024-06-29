'''2652. Sum Multiples

https://leetcode.com/problems/sum-multiples/description/
'''
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(1,n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum += i
        return sum