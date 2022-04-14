"""
  Approach:  Question says only that check if there's a cycle in directed graph if yes return False else True
  
         1 Using DFS: TC: O(N+E)   SC: O(2N)  AUX: O(N):
         
            Unlike undirected cycle detection, In this algo we will use 2 visited arrays:
                1. dfsVisited = [False]*v
                2. visited = [False]*v
                
            So when we visit the node via the recursion we will mark that node as visited in both the arrays
            so when the recursion for that perticular node is done we will again mark that node as unvisited in dfsVisited array
            By doing so if in any recursion we find a node visited in both the visited and dfsVisited array visited 
            we can say that there's a cycle in the Graph
            
                a. Create visited and dfsVisited arrays initialized with False
                b. loop for each component and pass node in hasCycle function
                c. In function mark node visited in both the arrays and run loop for each adj node
                d. if node is not visited in visited array than visit that node and mark it
                e. else check if its also visited in dfsVisited array if yes than return True
                
        2. Using Topological Sort BFS: 
            As we know topological sort works only on DAG so we take advantage,
            apply BFS topological sort using kanh's algo bfs and just count number of iterations of BFS  ie, while q
            if count == N: theres no cycle else cycle
         
     LeetCode 207: https://leetcode.com/problems/course-schedule/
     YT: https://www.youtube.com/watch?v=uzVUw90ZFIg&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=12
"""
############### DFS ################
class Solution:
    def canFinish(self, num: int, prereq: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(num)}
        for k, i in prereq:
            graph[k].append(i)
            
        
        def hasCycleDFS(node, graph):
            
            visited[node] = True
            dfs[node] = True
            
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True
                    if hasCycleDFS(i, graph): return True
                    
                elif dfs[i]: return True
                    
            dfs[node] = False
            return False
            
        
        dfs = [False]*num
        visited = [False]*num
        for i in range(num):
            if not visited[i]:
                visited[i] = True
                if hasCycleDFS(i, graph): return False
        return True
    
    
############ Using TopoSort BFS ############
class Solution:
    def canFinish(self, num: int, prereq: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(num)}
        for k, i in prereq:
            graph[k].append(i)
            
        indeg = [0]*num
        
        for i in range(num):
            for j in graph[i]:
                indeg[j] += 1
                
        q = deque()        
        for i in range(num):
            if indeg[i] == 0:
                q.append(i)
                
        c = 0
        while q:
            node = q.popleft()
            c += 1
            for i in graph[node]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
                    
        if c == num: return True
        return False
    
    
    
    
    
    
