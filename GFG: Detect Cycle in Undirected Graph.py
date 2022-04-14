"""
  Approach: 
    
        1. Using BFS: TC: O(N+E)    SC: O(N)
            In this we will check if the node is already visited and 
            by which parent its visited, if the node by which we came is not eq to visited node
            than there is a cycle........Poor explaination by me, Check the video
            
            Note: When we travase in the graph we travase for each connected and non connected components
                  IE, Check for all 0 to V
                  
            a. Take the visited array initially all marked as false
            b. check for 0 to v and create fn hasCycle to use bfs
            c. pass node in fn if not visited and mark as visited 
            d. create a queue with the value as [[node, -1]] where -1 initially coz theres no parent
            e. inside while q, pop(0) and mark node as visited 
            f. loop for all connections of node and check if visited or not if visited than check with prev, if child != prev return True
            
    GFG: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1#
    YT: https://www.youtube.com/watch?v=A8ko93TyOns
"""

def isCycle(self, v, adj):
        
        adj = {i:k for i, k in enumerate(adj)}
        def hasCycle(node, adj):
            visited[node] = True
            
            q = [[node, -1]]
            while q:
                
                node, prev = q.pop(0)
                visited[node] = True
                for c in adj[node]:
                    if not visited[c]:
                        q.append([c, node])
                    elif c == prev: continue
                    else: return True
                        
                        
        visited = [False]*v
        for i in range(v):
            if not visited[i]:
                if hasCycle(i, adj): return True
                
        return False
    
    
