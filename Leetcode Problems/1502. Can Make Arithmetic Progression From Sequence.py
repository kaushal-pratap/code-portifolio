'''1502. Can Make Arithmetic Progression From Sequence

https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] != diff:
                return False
        return True