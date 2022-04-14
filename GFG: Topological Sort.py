"""
    Topoligical Sort: The sorting of the vertexes of graph such that if 
                      edge exist between u and v than u must always come before v
                      It is done in only **Directed Acyclic Graph (DAG)**
                      there can be multiple sort order for a graph
                      
         1. Topological Sort Using DFS:   TC: O(N + E)   SC: O(2N)  AUX: O(N)
         
               Its nothing but travase the graph using DFS and after the end of each recursion 
               add the node in the stack, After whole travasal pop whole stack and push in another array 
               

"""
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


