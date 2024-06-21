'''43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        HashMap = {
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "0":0,
        }
        int1 = 0
        int2 = 0
        i = 0
        j = 0
        while i != len(num1)-1:
             int1 += HashMap[num1[i]]*(10**(len(num1)-1-i))
             i += 1
        int1 += HashMap[num1[i]]

        while j != len(num2)-1:
             int2 += HashMap[num2[j]]*(10**(len(num2)-1-j))
             j += 1
        int2 += HashMap[num2[j]]

        return str(int1*int2)

