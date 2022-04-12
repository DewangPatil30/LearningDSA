"""
Approach: Same as construct BT from inorder and preorder
          In BST, inorder travasal is a sorted array
          so we are given preorder trav we will sort the preorder to make inorder than
          using inorder and preorder we will construct the BST same as BT
          
          TC: O(N)  SC: O(N)
          
     LeetCode 1008: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
"""

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        inorder = sorted(preorder)
        ind = {k:i for i, k in enumerate(inorder)}
        
        def bst(l, r):
            if l > r: return 
            
            root = TreeNode(preorder.pop(0))
            root.left = bst(l, ind[root.val]-1)
            root.right = bst(ind[root.val]+1, r)
            
            return root
        
        return bst(0, len(inorder)-1)
