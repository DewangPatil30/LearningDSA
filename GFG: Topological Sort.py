"""
    Topoligical Sort: The sorting of the vertexes of graph such that if 
                      edge exist between u and v than u must always come before v
                      It is done in only **Directed Acyclic Graph (DAG)**
                      there can be multiple sort order for a graph
                      
         1. Using DFS:   TC: O(N + E)   SC: O(2N)  AUX: O(N)
               Its nothing but travase the graph using DFS and after the end of each recursion 
               add the node in the stack, After whole travasal pop whole stack and push in another array 
               
         2. Using BFS (Kanh's Algo):   TC: O(N + E)   SC: O(2N):
                a. Count the indegrees of all the nodes
                b. take q and append the all the nodes having indeg as 0
                c. BFS and add node to res array as soon as its popped
                d. check for nodes adj nodes and if present than decrement their indeg by 1 
                    if the indegree becmes 0 after decrement than add to q 
                    
                 return res
                 
       GFG: https://practice.geeksforgeeks.org/problems/topological-sort/1#
       YT: https://www.youtube.com/watch?v=rZv_jHZva34&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=14
"""
############ DFS #############
def topoSort(self, v, adj):
    def sort(node):
        visited[node] = True
        for i in adj[node]:
            if not visited[i]: sort(i)

        res.append(node)


    res = []
    visited = [False]*v
    for i in range(v):
        if not visited[i]: 
            visited[i] = True
            sort(i)

    return res[::-1]

############## BFS ############
def topoSort(self, v, adj):
        #Using BFS Kanh's Algo
        
        indeg = [0]*v       
        for i in range(v):
            for j in adj[i]:    #Counting Indegrees ie, no. of edges comming to node
                indeg[j] += 1
                
        q = deque()             #take q and append all nodes having indeg 0
        for i in range(v):
            if indeg[i] == 0:
                q.append(i)
                
        res = []        
        while q:                #simple BFS
            node = q.popleft()
            res.append(node)
            for i in adj[node]:
                indeg[i] -= 1   #decrement Indeg of adj node and if 0 after, add to queue
                if indeg[i] == 0:
                    q.append(i)
                    
        return res
    
    
