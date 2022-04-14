"""
  Approach:-
  
        Bipertite Graph: A graph which can be coloured using only 2 colours such that 
                         each Adjecent node must have opposit colours
                         
              If a graph have an odd length cycle, Its a Bipertite Graph, else Not bipertite graph
              
        1. Using BFS and Same logic as cycle detection in undirected graph:  TC: O(N+E)    SC: O(N):
                
                a. Create color array initialized with -1
                b. run the checkbpt for 0 -> len(graph)
                c. if fn if the node is not colored ie, color[node] == -1 color it with 0
                d. take q and append [node, 0] as value where 0 is color of that node
                e. run bfs and check if any adj node of cur node is colored 
                   if not than append in q as [adjnode, !color[cur node]]
                   and if colored is it same as cur node color
                   if yes than return 0

LeetCode 785: https://leetcode.com/problems/is-graph-bipartite/submissions/
YT: https://www.youtube.com/watch?v=nbgaEu-pvkU&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=10
"""
########### BFS ############
def checkbpt(node):
    if color[node] == -1:
        color[node] = 0

    q = [[node, color[node]]]

    while q:
        node, c = q.pop(0)
        for i in graph[node]:
            if color[i] == -1:
                color[i] = 0 if c == 1 else 1
                q.append([i, color[i]])
            elif color[i] == c: return True

    return False

color = [-1]*len(graph)
color[0] = 0

for i in range(len(graph)):
    if checkbpt(i): return False

return True

