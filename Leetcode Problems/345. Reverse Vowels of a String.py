'''345. Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/description/
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        s = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right] = s[right],s[left]
                right -= 1
                left += 1
                continue
            elif s[left] in vowels and s[right] not in vowels:
                right -= 1
                continue
            elif s[left] not in vowels and s[right] in vowels:
                left += 1
                continue
            right -= 1
            left += 1
        s = ''.join(s)
        return s