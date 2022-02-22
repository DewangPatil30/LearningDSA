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