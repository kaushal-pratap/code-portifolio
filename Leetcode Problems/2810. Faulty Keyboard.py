'''2810. Faulty Keyboard

https://leetcode.com/problems/faulty-keyboard/description/
'''

class Solution:
    def finalString(self, s: str) -> str:
        result = ''
        for i in s:
            if i != 'i':
                result += i
            else:
                result = result[::-1]
        return result