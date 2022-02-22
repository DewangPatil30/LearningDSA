def addNode(v):
    if v in graph:
        print('Node already present in graph')
        return
    
    graph[v] = []
    
def addEdge(v1, v2, weight=None, directed=False):
    if v1 not in graph:
        print(v1, 'not present in graph')
        return
    if v2 not in graph:
        print(v2, 'not present in graph')
        return
    
    
    if weight and directed:
        l2 = [v2, weight]
        graph[v1].append(l2)
    
    elif weight:
        l1 = [v1, weight]
        l2 = [v2, weight]
        
        graph[v1].append(l2)
        graph[v2].append(l1)
        
    elif directed:
        graph[v1].append(v2)
        
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
    

def printGraph():
    for i in graph:
        print(i, ': ', graph[i])




graph = {}

addNode('a')
addNode('b')
addNode('c')

addEdge('a', 'b', 10,  directed=True)
addEdge('c', 'b', 20, directed=True)
addEdge('a', 'd', 30, directed=True)

printGraph()
