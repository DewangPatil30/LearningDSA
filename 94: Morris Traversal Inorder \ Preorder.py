"""
Approach:                   Morris Travasal: 
            SPACIALITY: TC: Amotized O(N) and **SC: O(1) no memory usage

        Intution: Uses Threaded Binary Trees, ie, Connects root's left subtree's rightmost node with root, ie Threading
                  Therefore there is no need of stacking previous root 
        
        FOR Inorder Trav:--
        a. Take cur = root so root is not destroyed
        b. While cur:   
        c. If not cur.left: inord.append(cur.val) cur = cur.right
        d. Elif cur.left: take prev = cur.left
            While prev.right and prev.right != cur:      
                prev = prev.right
                
        e. If prev.right != cur:   prev.right = cur and cur = cur.left  ie, Connect cur's left subtree's rightmost node with cur and move left
            else its already pointing cur: so prev.right = None (remove thread),  inord.append(cur.val),  cur = cur.right
            
        FOR Preord:
        Same as inorder just append cur.val when creating the thread
        
        
        
     LeetCode 94 Inorder: https://leetcode.com/problems/binary-tree-inorder-traversal/
     LeetCode 144 Preorder: https://leetcode.com/problems/binary-tree-preorder-traversal/
     YT: https://www.youtube.com/watch?v=80Zug6D1_r4     
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Morris Travasal O(n) amotized O(1) space
        
        if not root: return
        cur = root
        inord = []

        while cur:
            
            if not cur.left:
                inord.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                    
                if prev.right != cur:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    inord.append(cur.val)       # For preord just shift this line to if statement above
                    cur = cur.right
        
        return inord
