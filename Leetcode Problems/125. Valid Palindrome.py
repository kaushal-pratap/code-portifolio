'''125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/description/
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        reverse_str = ''
        for i in s:
            if i.isalnum() == True:
                if i.isalpha() == True:
                    new_str += i.lower()
                    continue
                new_str += i
        left = 0
        right = len(new_str)-1
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True