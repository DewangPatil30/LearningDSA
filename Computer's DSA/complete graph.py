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
    

def delete_node(v):
    if v not in graph:
        print(v, ' node does not exist!')
        return
    
    graph.pop(v)
    for i in graph:
       for j in graph[i]:
           if j[0] == v:
               graph[i].pop(graph[i].index(j))
               break
           
    print(v, ' node deleted!')
    
    
def delete_edge(v1, v2, directed=False):
    if v1 not in graph or v2 not in graph:
        print(v1, ' or ', v2, ' node does not exist!')
        return
    
    for i in graph[v1]:
        if i[0] == v2:
            graph[v1].remove(i)
            break
        
    for i in graph[v2]:
        if i[0] == v1:
            graph[v2].remove(i)
            break    
        




def printGraph():
    for i in graph:
        print(i, ': ', graph[i])




graph = {}

addNode('a')
addNode('b')
addNode('c')

addEdge('a', 'b', 10)
addEdge('c', 'b', 20)
addEdge('a', 'd', 30)

printGraph()

print('Delete')
print('deleting node: ', 'a')
delete_node('a')
printGraph()
print()

print('deleting edge: ', 'b to c')
delete_edge('b', 'c')
printGraph()
print()


