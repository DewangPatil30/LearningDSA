    
class Bintree:
    
    def __init__(self, val = None):
        self.val = val
        self.right = None
        self.left = None
        
    def append(self, val):
        
        if self.val is None:
            self.val = val
            return
        
        q = [self]
        
        while q:
            
            node = q.pop(0)
            
            if not node.left:
                node.left = Bintree(val)
                break
            elif not node.right:
                node.right = Bintree(val)
                break    
            q.append(node.left)
            q.append(node.right)
            
    def preorder(self):
        
        print(self.val)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def level(self):
        if root is None:
            return []
        
        res = []
        q = [root]
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(level)
            
        return res
            

    
ele = [1,2,3,4,5,6,7,8]
root = Bintree()
for i in ele:
    root.append(i)
        
print
(root.level())
        
                
            
        
    
    
        