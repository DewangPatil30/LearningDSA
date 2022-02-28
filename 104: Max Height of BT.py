class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def md(root):
            if not root: return 0
            lft = md(root.left)
            ryt = md(root.right)
            
            return 1+max(lft, ryt)
        
        return md(root)
      
      
