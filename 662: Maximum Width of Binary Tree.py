"""
Approach:

    1. By applying the indexing to each node: TC: O(N)    SC: O(N)
    
        a. Create map m
        b. Create width fn for dfs
        c. We will use concept of children node indexes of root is: 
            for left child: 2 * rootInd+1
            for right child: 2 * rootInd+2
    
        d. We will only store the index of the first node of each level:
            ie, if level not in map: map[level] = pos
        e. each time calculate    maxw[0] = max( maxw[0], pos - map[level] + 1)
        f. Calls for dfs: 
            width(root.left, level+1, 2*pos+1) for left
            width(root.right, level+1, 2*pos+2) for right
            
         Return maxw[0]
         
    There is also the better sol
    
    LeetCode 662: https://leetcode.com/problems/maximum-width-of-binary-tree/
    YT: https://youtu.be/ZbybYvcVLks
"""

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        m = dict()
        maxw = [0]
        
        def width(root, d, pos):
            if root is None: return
            
            if d not in m:
                m[d] = pos
                
            maxw[0] = max(maxw[0], pos - m[d]+1)
                
            width(root.left, d+1, pos*2+1)
            width(root.right, d+1, pos*2+2)
            
        width(root, 0, 1)
        
        return maxw[0]

            
"""
PARTIAL SOLUTION {DOESN'T WORKS WITH LONG TESTCASES}
USING D-QUEUE: POP FRONT AND BACK TILL THEY ARE NULL 

"""            
            
            
        if not root: return 0
        q = [[root]]
        maxw = 1
        
        while q:
            level = q.pop(0)
            x = []
            
            for root in level:
                if not root:
                    x.append(root)
                    x.append(root)
                    continue
                    
                x.append(root.left)
                x.append(root.right)
                
            while x and (x[0] is None or x[-1] is None):
                if x[0] is None:
                    x.pop(0)
                if x[-1] is None:
                    x.pop()
                    
            maxw = max(maxw, len(x))
            
            if x:
                q.append(x)
                
        return maxw
            
            
                
            
            
        
