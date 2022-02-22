class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, values):
        if len(values) == 1:
            if self.data is None:
                self.data = values[0]
                return
            else:
                print('Root is not empty and parent is not provided')
                return
        else:
            if self.data == values[0]:
                if self.left is None:
                    self.left = BinaryTree(values[1])
                    return
                elif self.right is None:
                    self.right = BinaryTree(values[1])
                    return
                else:
                    temp = self.left
                    self.left = BinaryTree(values[1])
                    self.left.left = temp
                    return
            
            if self.left:
                self.left.insert(values)
            if self.right:
                self.right.insert(values)
            
        return
            
    def preorder(self):
        print(self.data, end=' ')
        
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    # def rightMost(obj):
    #     if obj.right:
    #         obj.right.rightMost()
    #     if obj.left:
    #         obj.left.rightMost()
        
    #     temp = obj.data
    #     obj.data = None
    #     print('Temp is: ', temp)
    #     return temp
    
    def remove(self, node):
        if self.data is None:
            print('the tree is empty!')
            return
        
        if self.data == node:
            if self.left is None:
                self.data = self.right.data
                self.right = None
                
            elif self.right is None:
                self.data = self.left.data
                self.left = None
            
            
    def level(self):
        if self is None:
            return []
        
        res = []
        q = [self]
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.data)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(level)
            
        return res
        
        
        
            
obj = BinaryTree(1)
lst =[(1,2), (1,3), (2,4), (3,8), (2,10)]

for i in lst:
    obj.insert(i)
    
print(obj.level())



            