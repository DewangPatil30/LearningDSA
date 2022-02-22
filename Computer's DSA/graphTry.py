nodes = []
graph = []
nCount = 0


def add_vertex(v):
    
    if v in nodes:
        print('node already exist')
        return 
    
    global nCount
    nCount += 1
    nodes.append(v)
    
    for i in graph:
        i.append(0)

    l = [0] * nCount
    graph.append(l)    
    
    
    
def add_edge(v1, v2, weight = 1, directed=False):
    
    if v1 not in nodes:
        print('node ', v1, ' not present')
        return
    elif v2 not in nodes:
        print('node ', v2, ' not present')
        return 
    
    idx1, idx2 = nodes.index(v1), nodes.index(v2)
    
    if directed: 
        graph[idx1][idx2] = weight
        return 
    
    graph[idx1][idx2] = graph[idx2][idx1] = weight 
    
    
    
def remove_vertex(v):
    if v not in nodes:
        print('The node %s not present' %v)
        return
    
    global nCount 
    nCount -= 1
    idx = nodes.index(v)
    nodes.pop(idx)
    
    graph.pop(idx)
    [i.pop(idx) for i in graph]
    
    
def remove_edge(v1, v2, directed=False):
    if v1 not in nodes:
        print('node %s not present in graph'%str(v1))
        return
    elif v2 not in nodes:
        print('node %s not present in graph'%str(v2))
        return
        
    idx1, idx2 = nodes.index(v1), nodes.index(v2)
    
    if directed: 
        graph[idx1][idx2] = 0
        return 
    
    graph[idx1][idx2] = graph[idx2][idx1] = 0
    
    
    

add_vertex('a')
add_vertex('b')
add_vertex('a')
add_vertex('c')

add_edge('a', 'b')
add_edge('b', 'c')


add_vertex('d')
add_edge('c', 'd')

add_vertex('e')
add_edge('d', 'e')


remove_vertex('d')

print(nodes)
[print(i) for i in graph]

add_edge('c', 'e')
print(nodes)
[print(i) for i in graph]