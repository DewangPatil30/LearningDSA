"""
GFG: https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1#
YT: https://www.youtube.com/watch?v=1ZGJzvkcLsA

tip: increment/decrement static after every loop
"""


class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        way = 0
        top, down, left, right = 0, r, 0, c
        res = []
        
        while top < down and left < right:
            
            if way == 0:        #For left -> right
                for i in range(left, right):
                   res.append(matrix[top][i])
                top += 1
                
            elif way == 1:      #For top -> down
                for i in range(top, down):
                    res.append(matrix[i][right-1])
                right -= 1
                
            elif way == 2:      #For right -> left
                for i in range(right-1, left-1, -1):
                    res.append(matrix[down-1][i])
                down -= 1
                
            elif way == 3:      #For down -> up
                for i in range(down-1, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
                
            way = (way+1) % 4
            
        return res
      
      
      
