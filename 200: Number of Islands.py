"""
Approaches:
        
        1. My approach (Explecite DFS): make up down left right function: TC: O(N*M)= O(N)    SC: O(N*M)   AUX: O(N)
        2. BFS:  Best For interview (for dfs replace popleft with pop): O(N*M)= O(N)    SC: O(2*N*M)   AUX: O(N)
        3. Advanced DFS

LeetCode 200: https://leetcode.com/problems/number-of-islands/
YT: https://www.youtube.com/watch?v=pV2kpPD66nE
"""

__________________________________________________________________________________________________________________________________________________________________    
------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def numIslands(self, grid):     #My Approach
        def up(i, j, r, c):
            if i < 0 or grid[i][j] == '0': return 

            grid[i][j] = 'V'

            left(i, j-1, r, c)
            right(i, j+1, r, c)
            down(i+1, j, r, c)
            up(i-1, j, r, c)

        def down(i, j, r, c):
            if i >= r or (i, j) in visited or grid[i][j] == '0': return 

            grid[i][j] = 'V'

            left(i, j-1, r, c)
            right(i, j+1, r, c)
            up(i-1, j, r, c)
            down(i+1, j, r, c)

        def left(i, j, r, c):
            if j < 0 or (i, j) in visited or grid[i][j] == '0': return 

            grid[i][j] = 'V'

            right(i, j+1, r, c)
            down(i+1, j, r, c)
            up(i-1, j, r, c)
            left(i, j-1, r, c)

        def right(i, j, r, c):
            if j >= c or (i, j) in visited or grid[i][j] == '0': return 

            grid[i][j] = 'V'

            left(i, j-1, r, c)
            down(i+1, j, r, c)
            up(i-1, j, r, c)
            right(i, j+1, r, c)


        visited = set()

        res = 0
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):

                if grid[i][j] == '1' and (i, j) not in visited:
                    up(i-1, j, r, c)
                    down(i+1, j, r, c)
                    left(i, j-1, r, c)
                    right(i, j+1, r, c)

                    res += 1

        return res
    
__________________________________________________________________________________________________________________________________________________________________    
------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def numIslands(self, grid):     #BFS / DFS Interview
        def bfs(i, j, row, col):
            visited.add((i, j))
            q = collections.deque()
            q.append((i, j))
            direction = [[1,0], [-1, 0], [0, 1], [0, -1]]

            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for dr, dc in direction:

                    r, c = i+dr, j+dc
                    if (r in range(row) and c in range(col) and
                        (r, c) not in visited and
                        grid[r][c] != '0'):

                        q.append((r, c))

        visited = set()
        res = 0
        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for j in range(c):

                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j, r, c)
                    res += 1

        return res  
    
__________________________________________________________________________________________________________________________________________________________________    
------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] != '1':
            return
        
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    
__________________________________________________________________________________________________________________________________________________________________    
------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
