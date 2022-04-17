"""
  Approaches:
        
            1. Store nodes in Inorder than rearrange: O(N)  O(N)
            2. Travasal Inorder while Rearranging: O(N)   O(H):
            
  LeetCode 897: https://leetcode.com/problems/increasing-order-search-tree/
"""
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inord(root):
            if not root: return 
            
            inord(root.left)
            
            root.left = None
            cur[0].right = root
            cur[0] = root
        
            inord(root.right)
            
        cur = [TreeNode(None)]
        ans = cur[0]
        
        inord(root)
        return ans.right
        
