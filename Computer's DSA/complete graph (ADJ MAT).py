def addNode(v):
    global nCount
    
    if v in nodes:
        print('already present')
        return
    
    nCount += 1
    nodes.append(v)
    
    #for adding new column for added node
    for i in graph:
        i.append(0)
    
    # adding new row to adj matrix
    temp = [0] * nCount
    graph.append(temp)
    
def addEdge(v1, v2, weight=1, directed=False):
    
    if v1 not in nodes or v2 not in nodes:
        print('Node not present in the graph')
        return 
    
    index1 = nodes.index(v1)
    index2 = nodes.index(v2)
    
    if directed:
        graph[index1][index2] = weight
        return
    
    graph[index1][index2] = graph[index2][index1] = weight
    
    
def delete_node(v):
    global nCount
    if v not in nodes:
        print(v, ' node does not exist!')
        return
    
    index = nodes.index(v)
    nCount -= 1
    nodes.pop(index)
    
    graph.pop(index)
    for i in graph:
        i.pop(index)
        
    print(v, ' node deleted!')
    
def delete_edge(v1, v2, directed=False):
    if v1 not in nodes or v2 not in nodes:
         print(v1, ' or ', v2, ' node does not exist!')
         return
     
    index1 = nodes.index(v1)
    index2 = nodes.index(v2)
    
    if directed:
        graph[index1][index2] = 0
        return
    
    graph[index1][index2] = graph[index2][index1] = 0 
    
def pGraph():
    print("nodes are: ", nodes)
    
    for i in range(nCount):
        for j in range(nCount):
            print(format(graph[i][j]), end=' ')
        print()

nodes = []
graph = []
nCount = 0

print('Before adding')
pGraph()
print('after adding')
addNode('A')
addNode('B')
addNode('C')

addEdge('A', 'C')
addEdge('B', 'C', weight=20)
addEdge('C', 'A', weight=30, directed=True)
pGraph()

print('deleting "A" node')
delete_node('A')
pGraph()

print('deleting "B" to "C" edge')
delete_edge('B', 'C', directed=True)
pGraph()



