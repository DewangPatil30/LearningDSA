"""
Approach: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        
        3                          3                          .  3 .
    [9]    [15, 20, 7]  ----> 9         20                 9       . 20 .
                                    [15]    [7]  ---->          15        7
        
    Take root val from preorder
    and root.left = recursive(l, index of root.val-1)
        root.right = recursive(index of root.val+1, r)
        
        return root


        FOR POSTORDER:
        Same as preorder just instead of pop(0) we use pop() and call for root.right will come first than for left

    LeetCode 105: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    YT Strivers: https://youtu.be/aZNaLrVebKQ
"""

# FOR PREORDER
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        m = {k: i for i, k in enumerate(inorder)}
        
        def constructTree(l, r):
            
            if l > r:
                return 
            
            root = TreeNode(preorder.pop(0))
            mid = root.val
            
            root.left = constructTree(l, m[mid]-1)
            root.right = constructTree(m[mid]+1, r)
            
            return root
        
        
        return constructTree(0, len(preorder)-1)
        
        
# FOR PREORDER
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        ind = {k:i for i, k in enumerate(inorder)}
        
        def constructTree(l, r):
            if l > r: return 
            
            root = TreeNode(postorder.pop())  # Change 1
            mid = root.val
            
            root.right = constructTree(ind[mid]+1, r) #Change 2
            root.left = constructTree(l, ind[mid]-1)
            
            return root
            
        
        return constructTree(0, len(postorder)-1)
