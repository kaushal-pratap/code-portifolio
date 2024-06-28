'''74. Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/description/
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True