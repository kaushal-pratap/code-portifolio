'''1342. Number of Steps to Reduce a Number to Zero

https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 0:
                step += 1
                num = num // 2
            else:
                num -= 1
                step += 1
        return step