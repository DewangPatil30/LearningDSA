"""
|----------------------------------------------------Method #1: Pure DFS -------------------------------------------------------------|
"""

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def listcheck(root, head):
            
            if not head: 
                res[0] = True
                return 
        
            elif not root: return
            
            if root.val == head.val:
                listcheck(root.left, head.next)
                listcheck(root.right, head.next)
        
        
        def preord(root, head):
            if not root: return 
            
            if root.val == head.val:
                listcheck(root, head)
                
                
            preord(root.left, head)
            preord(root.right, head)
            
        res = [False]
        preord(root, head)
        return res[0]
      
"""
|----------------------------------------------------Method #2: DFS + BFS using HashSet -------------------------------------------------------------|
"""

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
		def listchk(head, root):
            if not head:
                return True
            if root and head.val == root.val:
                return (listchk(head.next, root.left) or
                        listchk(head.next, root.right))
            return False

        row = {root}
        while row:
            nextrow = set()
            for root in row:
                if root.val == head.val and listchk(head, root):
                    return True
                if root.left:
                    nextrow.add(root.left)
                if root.right:
                    nextrow.add(root.right)
            row = nextrow

        return False
      
