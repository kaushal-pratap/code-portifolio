'''7. Reverse Integer

https://leetcode.com/problems/reverse-integer/description/
'''

class Solution:
    def reverse(self, x: int) -> int:
        i = len(str(x))-1
        new = ''
        while i >= 0:
            new += str(x)[i]
            i -= 1
        if x < 0:
            new = -int(new[:len(new)-1])
        return int(new)
