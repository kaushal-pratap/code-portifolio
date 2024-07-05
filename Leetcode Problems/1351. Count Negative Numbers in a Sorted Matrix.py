'''1351. Count Negative Numbers in a Sorted Matrix

https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
'''

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        new = []
        for i in grid:
            new += i 

        for j in new:
            if j < 0:
                count += 1 

        return count