"""
Approach: 
    Just like computing max height of BT, 
    Diameter of BT is (Left height + Right height)
    
    Same compute leftH and rightH by max height prog
    res[0] = max(res[0], lh+rh)
    
    return 1 + max(lh, rh)
    in main: return res[0]
    
  LeetCode 543: https://leetcode.com/problems/diameter-of-binary-tree/
"""
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameter(root):
            if not root: return 0
            
            l = diameter(root.left)
            r = diameter(root.right)
            
            res[0] = max(res[0], l+r)
            
            return 1 + max(l, r)
            
        
        res = [0]
        diameter(root)
        return res[0]
