'''258. Add Digits

https://leetcode.com/problems/add-digits/description/
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        remainder = num % 9
        if remainder == 0:
            return remainder + 9
        return remainder
