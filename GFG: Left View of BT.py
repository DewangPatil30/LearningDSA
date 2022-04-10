"""
Approaches:
        
    1. Using Recursion: TC: O(N)   SC: O(N) stack memory
        Preorder Travarsal
        
        a. Preord function takes args as (root, currlevel, prevLevel)
            initially currlevel = 1 and prevlevel = 0
        b. if not root: return
           if prevlevel < currlevel:
                lview.append(root.data)
                prevlevel = currlevel
           
           preord(root.left, currlevel+1, prevlevel) -----so for left only it will work
           preord(root.right, currlevel+1, prevlevel) -------for right only if left has no child but right have
                
      2. Level Order: TC: O(N) SC: O(N)
         
         a. q = [root]
         b. while q:
                for i in range len q:
                    root = q.pop(0)
                    if i == 0: lview.append(root.data)
                    if root.left: q.append left
                    same append right
                    
    GFG: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1#
    EDITORIAL: https://www.geeksforgeeks.org/print-left-view-binary-tree/
    
"""
def LeftView(root):
    
    if not root: return []
    
    lview = []
    q = [root]
    while q:
        for i in range(len(q)):
            root = q.pop(0)
            
            if i == 0: lview.append(root.data)
            
            if root.left: q.append(root.left)
            if root.right: q.append(root.right)        
        
            
    return lview

