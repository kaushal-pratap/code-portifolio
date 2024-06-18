'''  73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

'''

class Solution:

    def __init__(self):
        self.HashMap = {}
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        j = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.HashMap[str(i),str(j)] = 0
                    
        for k in self.HashMap:
            i = int(k[0])
            j = int(k[1])
            
            for a in range(m):
                matrix[a][j] = 0
            for b in range(n):
                matrix[i][b] = 0
            