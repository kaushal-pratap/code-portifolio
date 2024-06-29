'''2119. A Number After a Double Reversal

https://leetcode.com/problems/a-number-after-a-double-reversal/description/
'''

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(str(num)) == 1:
            return True

        if str(num)[len(str(num))-1] != '0':
            return True
        return False