"""
   Approaches: 
        
        1. Inorder trav:   tc: O(N)  sc: O(N) aux stack space
                a. Maintain list var res = [0] and i = [0]
                b. do inorder trav,   if i[0] < k: res[0] = root.val, else: return      (bcoz i[0] == k so we got ans)
                return res[0]
                
        2. Moris Inorder trav:  tc: O(N)  sc: O(1) 
                Same as Normal inorder trav, maintain counter and kth 
                as soon as counter == k break and return kth

      LeetCode 230: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
      YT: https://www.youtube.com/watch?v=9TJYWh0adfk
"""

###### Moris Inorder #######
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cur, cnt, kth = root, 0, 0
        
        while cur and cnt < k:
            
            if not cur.left:
                kth = cur.val
                cnt += 1
                cur = cur.right
            else:
                
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                    
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    kth = cur.val
                    cnt += 1
                    cur = cur.right
                
        return kth
        
######## Regular Inorder #######
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def small(root, k):
            if not root:return 
            
            small(root.left, k)
            
            if i[0] < k: res[0] = root.val
            else: return 
            i[0] += 1
            
            small(root.right, k)
            
        res = [0]
        i = [0]
        small(root, k)
        
        return res[0]

