'''367. Valid Perfect Square

https://leetcode.com/problems/valid-perfect-square/
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            if i*i > num:
                break
            if i*i == num:
                return True
        return False