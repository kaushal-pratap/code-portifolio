'''415. Add Strings

https://leetcode.com/problems/add-strings/description/
'''

import sys
sys.set_int_max_str_digits(6000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        HashMap = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        int_1 = 0
        int_2 = 0
        for i in range(len(num1)):
            int_1 += HashMap[num1[i]]*(10**(len(num1)-1-i))

        for j in range(len(num2)):
            int_2 += HashMap[num2[j]]*(10**(len(num2)-1-j))
        
        return (str(int_1 + int_2))