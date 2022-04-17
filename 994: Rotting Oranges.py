"""
  Approach: 
  
        1. Using BSF:  O(MxN) O(MxN)
            a. count num of fresh orngs and push pos of rotten oranges in q in one iteration
            b. BFS append q as list in a deque
            c. while dq-----pop for i, j in popedlist    r = i + dr, c = j + dc for dr, dc in dire
            d. if r in range row and c in range col and grid[r][c] == 1: grid[r][c] = 2, cnt += 1, temp.append([r,c])
            e. if temp: dq.append(temp)
            f. if dq: days += 1
            return -1 if cnt != freshCount else days

LeetCode 994: https://leetcode.com/problems/rotting-oranges/
YT: https://www.youtube.com/watch?v=pUAPcVlHLKA
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfs(row, col, q, fresh):
            
            days = 0
            cnt = 0
            dq = deque()
            dq.append(q)
            
            dire = [[1,0], [-1,0], [0,1], [0,-1]]
            
            while dq:
                q = dq.popleft()
                temp = []
                for i, j in q:
                    for dr, dc in dire:
                        r = i + dr
                        c = j + dc
                        
                        if r in range(row) and c in range(col) and grid[r][c] == 1:
                            grid[r][c] = 2
                            temp.append([r,c])
                            cnt += 1
                            
                
                if temp: dq.append(temp)                
                if dq: days += 1
                
            print(grid)
            if fresh != cnt: return -1
            return days
            

        row, col = len(grid), len(grid[0])
        
        q = []
        fcount = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fcount += 1
                    
        return bfs(row, col, q, fcount)
    
    
