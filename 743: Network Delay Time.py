"""
  Approach: 
  
        1. Using BFS: 
            Easier version of shortest path in DAG, dont need to toposort just strt from scr node
            1. create dist arr initialized with inf except src node = 0
            2. q.append(src)
            3. BFS--------- for i in adj[node]: 
            4. d = dist[node] + i.weight       # same as dist[node] + 1
            5. if dist[i] > d: dist[i] = d, q.append(i)
            
            return max(dist) if all( i != inf for i in dist) else -1
            
        2. Dijkstrae Algo: TODO
 
 LeetCode 743: https://leetcode.com/problems/network-delay-time/
 YT: https://www.youtube.com/watch?v=CrxG4WJotgg&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=17
"""

class Signal:
    def __init__(self, node, w):
        self.node = node
        self.weight = w
        

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        m = {i:[] for i in range(1, n+1)}
        for t in times:
            m[t[0]].append(Signal(t[1], t[2]))
            
        dist = [inf]*(n+1)
        dist[0] = 0
        dist[k] = 0
        
        q = deque()
        q.append(k)
        
        while q:
            
            node = q.popleft()
            for ad in m[node]:
                d = dist[node] + ad.weight
                if dist[ad.node] > d:
                    dist[ad.node] = d
                    q.append(ad.node)
                    
        if any(i == inf for i in dist): return -1
        return max(dist)
                
