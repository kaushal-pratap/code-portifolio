'''989. Add to Array-Form of Integer

https://leetcode.com/problems/add-to-array-form-of-integer/description/
'''

import sys
sys.set_int_max_str_digits(16000)
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        result =[]
        new_num = ''
        for i in num:
            new_num += str(i)
        new_num = int(new_num) + k
        for j in str(new_num):
            result.append(int(j))
        return result