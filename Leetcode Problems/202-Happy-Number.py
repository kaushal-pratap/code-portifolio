'''202 Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

class Solution:
    def __init__(self):
        self.HashMap = {}
    def isHappy(self, n: int):
        total_sum = 0
        for i in str(n):
            i = int(i)
            total_sum += i**2
        if total_sum == 1:
            return True
        else:
            if n in self.HashMap:
                self.HashMap = {}
                return False

            self.HashMap[n] = total_sum
            return self.isHappy(total_sum)

