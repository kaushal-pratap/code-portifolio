'''66. Plus One

https://leetcode.com/problems/plus-one/description/
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        array = []
        number = ''
        for i in digits:
            number += str(i)
        number = int(number) + 1
        for j in str(number):
            array.append(int(j))
        return array