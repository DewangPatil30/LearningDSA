"""
Approach:
    
    1. Level order Travasal: TC: O(Levels * N log N) SC: O(N):-
    
        a. Strt with q = [[[0 #for vertical level, root]]]
        b. Take a map in which we will store node vals via vertical level
        
        c. While q, each time sort the  level ie, q[0] by the val of node
            q[0].sort(key = lambda x: x[1].val) 
            
        d. Run For loop for each node inside q[0]:
            if q[0][0] not in map---- map[q[0][0]] = []
            map[q[0][0]].append(q[0][1].val)
            
         e. If left: x.append([v-1, root.left]) same for right bas v+1
         f. at last take sorted keys and append(m[key]) in res 
         return res
         
     LeetCode 987: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        verti = []
        q = [[[0, root]]]
        m = {}
        
        while q:
            
            q[0].sort(key=lambda x: x[1].val)
            temp = q.pop(0)
            x = []
            
            for t in temp:
                
                v, root = t
                if v not in m: m[v] = []
                m[v].append(root.val)
                    
                if root.left: x.append([v-1, root.left])
                if root.right: x.append([v+1, root.right])
                    
            if x: q.append(x)
                
                
        for v in sorted(m): verti.append(m[v])
            
        return verti
