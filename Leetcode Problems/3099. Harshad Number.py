'''3099. Harshad Number

https://leetcode.com/problems/harshad-number/description/
'''

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        for i in str(x):
            sum += int(i)
        if x % sum == 0:
            return sum
        return -1