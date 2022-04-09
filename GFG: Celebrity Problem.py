"""
  Approaches:
        
        1. check if any row r contains all the 0's, if found check if all mat[i][r] is 1
            If yes than R is the celebrity. TC: O(N*N) SC: O(1)
            
        2. Using Stack: TC O:(N) SC:O(N)
           
            a. Push all indexes of rows till n in the stack
            b. Pop 2 rows out and store in a, b 
            c. if mat[a][b] == 0 ie if a dont know b than b cant be celebrity
                Push a back in stack else push b in stack
            apply step c till stack len != 1
            d. Now only one index is in stack check if all mat[i][celeb] == 1 where i != celeb
            if true return Celeb else -1
            
        GFG: https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1#
        YT: https://www.youtube.com/watch?v=CiiXBvrX-5A
        
"""

class Solution:
    
    def celebrity(self, mat, n):
        # code here
        
        st = []
        for i in range(n):
            st.append(i)
            
        while len(st) > 1:
            a, b = st.pop(), st.pop()
            
            if mat[a][b] == 0: st.append(a)
            else: st.append(b)
            
        pot = st[-1]
        for i in range(n):
            if i != pot and mat[i][pot] == 0:
                return -1
        for i in range(n):
            if i != pot and mat[pot][i] == 1:
                return -1
        
        return pot
        
         # Code for brute force N^2 approach
        if False:    
            res = -1
            found = False
            knowsJ = [0]*n
            Jknows = [0]*n
            
            for i in range(n):
                for j in range(n):
                    if mat[i][j] == 1:
                        knowsJ[j] += 1
                    if mat[j][i] == 1:
                        Jknows[j] += 1
                        
            for i in range(n):
                if knowsJ[i] == n-1 and Jknows[i] == 0:
                    if found: return -1
                    
                    found = True
                    res = i
            
            return res
