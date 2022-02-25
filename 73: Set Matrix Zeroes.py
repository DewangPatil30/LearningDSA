class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def up(r, c):
            if r < 0 or matrix[r][c] == 0:
                return 
            
            matrix[r][c] = 'X'
            up(r-1, c)
        
        def down(r, c):
            if r == row or matrix[r][c] == 0:
                return 
            
            matrix[r][c] = 'X'
            down(r+1, c)
        
        def left(r, c):
            if c < 0  or matrix[r][c] == 0:
                return 
            
            matrix[r][c] = 'X'
            left(r, c-1)
        
        def right(r, c):
            if c == col or matrix[r][c] == 0:
                return 
            
            matrix[r][c] = 'X'
            right(r, c+1)
        
        
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'X'
                    
                    up(i-1, j)
                    down(i+1, j)
                    left(i, j-1)
                    right(i, j+1)
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0
                    
        
