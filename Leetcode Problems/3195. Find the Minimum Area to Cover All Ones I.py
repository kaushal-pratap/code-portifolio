'''3195. Find the Minimum Area to Cover All Ones I

https://leetcode.com/contest/weekly-contest-403/problems/find-the-minimum-area-to-cover-all-ones-i/description/
'''

class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        i_array = []
        j_array = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    i_array.append(i)
                    j_array.append(j)
        width = (max(j_array) - min(j_array)) + 1
        length = (max(i_array) - min(i_array)) + 1
        return width*length
        