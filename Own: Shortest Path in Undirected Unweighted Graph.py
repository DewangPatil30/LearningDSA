"""
Approach:
        
        1 Using BFS: 
            Create dist array initialized with inf except src index value will be 0 coz src -> src = 0
            now bfs 
            if cur dist = dist[node] + 1  #to reach curNode
            if dist[curNode] > cur dist: q.append(curNode) dist[curNode] = curDist
            
           
"""
from math import *
from collections import *

if __name__ == "__main__":
    adj = [[1,3], [0,2,3], [1,6], [0,4], [3,5], [4,6], [2,5,7,8],
           [6,8], [6,7]]
    
    dist = [0] + [inf]*(len(adj)-1)
    q = deque()
    q.append(0)
    
    while q:    
        node = q.popleft()
        
        for i in adj[node]:
            d = 1 + dist[node]
            if dist[i] > d: 
                q.append(i)
                dist[i] = d
                
    print(dist)
    
